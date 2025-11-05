import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

#   FUNCIÓN PRINCIPAL — FEATURE ENGINEERING
def prepare_features(df, target="Churn"):
    
    # 1) Convertir variable objetivo a numérica
    df[target] = df[target].map({"Yes": 1, "No": 0})

    # 2) Separar X / y
    X = df.drop(columns=[target])
    y = df[target]

    # 3) Identificar tipos de variables
    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(include=["object", "bool"]).columns.tolist()

    # Si hubiera columnas ordinales, definirlas aquí
    ordinal_features = []

    # Categóricas nominales = todas las categóricas que NO sean ordinales
    cat_nominal_features = [c for c in categorical_features if c not in ordinal_features]

    # 4) Pipelines por tipo de dato

    numeric_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("ohe", OneHotEncoder(handle_unknown="ignore"))
    ])

    ordinal_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("ordinal", OrdinalEncoder())
    ])

    # 5) ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, cat_nominal_features),
            ("ord", ordinal_pipeline, ordinal_features)
        ]
    )

    # 6) Split Train / Test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # 7) Aplicar transformaciones
    X_train_t = preprocessor.fit_transform(X_train)
    X_test_t = preprocessor.transform(X_test)

    # Retornar datos listos para entrenar
    return preprocessor, X_train_t, X_test_t, y_train, y_test

#   load_data()
def load_data(path="../../Base_de_datos.csv", target="Churn"):
    """
    Carga CSV y ejecuta feature engineering completo.
    Retorna preprocessor + splits lista para entrenamiento.
    """
    df = pd.read_csv(path)
    return prepare_features(df, target)


#   MAIN
if __name__ == "__main__":
    preprocessor, X_train, X_test, y_train, y_test = load_data()
    print(" Feature Engineering listo!")
