import pandas as pd
import numpy as np

from scipy.stats import ks_2samp, chi2_contingency
from scipy.spatial.distance import jensenshannon


# =========================================================
# PSI
# =========================================================
def psi_score(expected, actual, bins=10):
    expected_perc = np.histogram(expected, bins=bins)[0] / len(expected)
    actual_perc   = np.histogram(actual, bins=bins)[0] / len(actual)

    psi = np.sum(
        (actual_perc - expected_perc) * 
        np.log((actual_perc + 1e-8) / (expected_perc + 1e-8))
    )
    return psi


# =========================================================
# Data Drift
# =========================================================
def compute_drift(baseline_df, new_df):
    drift_results = []

    for col in baseline_df.columns:

        # -------- NUMERICAL --------
        if baseline_df[col].dtype != "object":
            ks_stat, ks_p = ks_2samp(
                baseline_df[col].dropna(),
                new_df[col].dropna()
            )

            psi = psi_score(
                baseline_df[col].dropna(),
                new_df[col].dropna()
            )

            drift_results.append({
                "feature": col,
                "type": "numerical",
                "ks_pvalue": round(ks_p, 4),
                "psi": round(psi, 4),
                "js_distance": None,
                "chi_pvalue": None
            })

        # -------- CATEGORICAL --------
        else:
            categories = list(
                set(baseline_df[col].dropna().unique()) |
                set(new_df[col].dropna().unique())
            )

            base_counts = baseline_df[col].value_counts(normalize=True)
            new_counts  = new_df[col].value_counts(normalize=True)

            base_dist = np.array([base_counts.get(cat, 0) for cat in categories])
            new_dist  = np.array([new_counts.get(cat, 0) for cat in categories])

            # Jensen–Shannon distance
            js = jensenshannon(base_dist, new_dist)

            # Chi–square test → ahora bien formateado
            contingency = pd.DataFrame({
                "baseline": base_dist,
                "new": new_dist
            }).T

            chi2, chi_p, _, _ = chi2_contingency(contingency)

            drift_results.append({
                "feature": col,
                "type": "categorical",
                "ks_pvalue": None,
                "psi": None,
                "js_distance": round(float(js), 4),
                "chi_pvalue": round(chi_p, 4)
            })

    return pd.DataFrame(drift_results)



# =========================================================
# MAIN
# =========================================================
if __name__ == "__main__":
    print("\n=== Running Monitoring ===")

    baseline = pd.read_csv("../../Base_de_datos.csv")
    new_data = pd.read_csv("../../Base_de_datos.csv")   # simulado

    drift_table = compute_drift(baseline, new_data)

    print("\n=== Data Drift Results ===")
    print(drift_table)

    # Crear carpeta si no existe
    import os
    os.makedirs("../monitoring", exist_ok=True)

    drift_table.to_csv("../monitoring/data_drift_report.csv", index=False)
    print("\n✅ Report saved in: ../monitoring/data_drift_report.csv")
