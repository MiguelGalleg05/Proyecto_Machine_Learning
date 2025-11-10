import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from ft_engineering import load_data   

# Función: resumen de métricas
def summarize_classification(y_true, y_pred, y_prob=None):

    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
    }

    if y_prob is not None:
        metrics["roc_auc"] = roc_auc_score(y_true, y_prob)

    return metrics

# Función: entrenamiento + evaluación
def build_model(model_name, model, X_train, y_train, X_test, y_test):

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
    else:
        y_prob = None

    metrics = summarize_classification(y_test, y_pred, y_prob)
    metrics["model"] = model_name

    return model, metrics

# MAIN
if __name__ == "__main__":

    
    preprocessor, X_train, X_test, y_train, y_test = load_data()

    # Modelos a comparar
    models = {
        "LogReg": LogisticRegression(max_iter=1000),
        "DecisionTree": DecisionTreeClassifier(),
        "RandomForest": RandomForestClassifier(n_estimators=200),
        "XGBoost": XGBClassifier(
            eval_metric="logloss",
            learning_rate=0.1,
            max_depth=5,
            n_estimators=200,
            subsample=0.8
        ),
    }

    results = []
    trained_models = {}

    # Entrenamiento + evaluación
    for name, mdl in models.items():
        print(f"\n🔹 Entrenando: {name}")

        model, metrics = build_model(
            name,
            mdl,
            X_train,
            y_train,
            X_test,
            y_test
        )

        trained_models[name] = model
        results.append(metrics)

    # Tabla comparativa
    results_df = pd.DataFrame(results)
    print("\n Resultados comparativos:")
    print(results_df.sort_values(by="f1", ascending=False))

    # Mejor modelo
    best_model_name = results_df.sort_values(by="f1", ascending=False).iloc[0]["model"]
    best_model = trained_models[best_model_name]

    print(f"\n Mejor modelo: {best_model_name}")



    # Gráfico comparativo
    plt.figure(figsize=(8,4))
    plt.bar(results_df["model"], results_df["f1"], 
        color="skyblue", edgecolor="black")
    plt.title("Comparación de modelos - F1 Score")
    plt.ylabel("F1 Score")
    plt.xlabel("Modelo")
    plt.show()



    # Opcional: Guardar modelo ganador
    joblib.dump(best_model, "../models/best_model.pkl")
    print(" Modelo guardado en ../models/best_model.pkl")
