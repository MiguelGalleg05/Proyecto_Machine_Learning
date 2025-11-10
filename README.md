##vProyecto de Machine Learning

Pipeline modular para un problema supervisado de clasificación (Churn)

📌 Descripción

Este proyecto implementa un pipeline completo de Machine Learning para resolver un problema supervisado tipo clasificación, desde la carga de datos hasta el despliegue del modelo.

El flujo incluye:

* Carga y validación de datos

* Análisis Exploratorio (EDA)

* Feature Engineering

* Entrenamiento de múltiples modelos

* Evaluación comparativa

* Selección y guardado del mejor modelo

* Monitoreo (Data Drift)

* Exposición vía API

* Contenerización con Docker

🎯 Objetivos

✅ Desarrollar pipeline ML modular
✅ Entrenar múltiples modelos y seleccionar el mejor
✅ Realizar monitoreo periódico del modelo
✅ Exponer el modelo mediante API
✅ Desplegar como contenedor Docker

📂 Estructura del Proyecto
Proyecto_Machine_Learning/
│
├── data/                             # Datos
│   ├── Base_de_datos.csv             # Dataset original
│   └── monitoring/
│       └── data_drfit_report.csv     # Resultados medición drift
│
├── mlops_pipeline/
│   └── src/
│       ├── Cargar_datos.ipynb        # Carga inicial
│       ├── compresion_eda.ipynb      # EDA completo
│       ├── ft_engineering.py         # Feature Engineering
│       ├── model_training.ipynb      # Entrenamiento
│       ├── model_training_evaluation.py # Evaluación
│       ├── model_evaluation.ipynb    # Métricas
│       ├── model_monitoring.ipynb    # Monitoreo
│       ├── model_monitoring.py       # Data Drift
│       ├── model_deploy.ipynb        # Despliegue
│       ├── model_deploy.py           # API
│       └── utils/                    # Módulos auxiliares
│
├── models/
│   └── best_model.pkl                # Mejor modelo
│
├── app/
│   └── streamlit_app.py              # UI Monitoreo
│
├── Dockerfile
├── requirements.txt
├── config.json
├── set_up.bat
└── README.md

✅ Funcionalidades Principales

✔ Carga / Limpieza de datos
✔ Análisis Exploratorio (EDA)
✔ Ingeniería de características
✔ Entrenamiento de múltiples modelos
✔ Selección del mejor modelo
✔ Métricas de desempeño
✔ Monitoreo de data drift
✔ API predictiva (FastAPI)
✔ Contenerización (Docker)
✔ Visualización Streamlit

⚙ Configuración (config.json)
{
  "data": {
    "input_path": "data/Base_de_datos.csv",
    "target_column": "Churn",
    "test_size": 0.2,
    "random_state": 42
  },
  "model": {
    "type": "RandomForestClassifier",
    "params": {
      "n_estimators": 200,
      "max_depth": null
    }
  },
  "output": {
    "model_path": "models/best_model.pkl",
    "reports": "data/monitoring/"
  }
}

🧰 Instalación del entorno
✅ Crear entorno
python -m venv venv

✅ Activar entorno

Windows:

venv\Scripts\activate


MacOS / Linux:

source venv/bin/activate

✅ Instalar dependencias
pip install -r requirements.txt

🚀 Ejecución del Pipeline
1️⃣ Carga / Limpieza

📄 Cargar_datos.ipynb

2️⃣ Análisis Exploratorio (EDA)

📄 compresion_eda.ipynb

Incluye:

Describe

Distribuciones

Outliers

Correlación

Relaciones con variable objetivo

3️⃣ Feature Engineering

📄 ft_engineering.py

Incluye:

Encoding

Escalado

Imputación

División train/test

4️⃣ Entrenamiento

📄 model_training.ipynb

Entrena múltiples modelos:

Logistic Regression

RandomForest

XGBoost

LightGBM

5️⃣ Evaluación

📄 model_training_evaluation.py

Se selecciona el mejor modelo

Se guarda como .pkl en /models/

6️⃣ Monitoreo (Data Drift)

📄 model_monitoring.py

Métricas:

KS Test

PSI

Jensen-Shannon

Chi²

Genera:

data/monitoring/data_drift_report.csv

7️⃣ API para predicción

📄 model_deploy.py

Iniciar API:

uvicorn mlops_pipeline.src.model_deploy:app --reload

8️⃣ Streamlit UI

📄 streamlit_app.py

streamlit run streamlit_app.py

📊 Métricas disponibles

Accuracy

Precision

Recall

F1-Score

ROC-AUC

KS

PSI

Chi²

JS Divergence

🧩 Feature Engineering

Incluye:

Scaling

Encoding

Selección de variables

Imputación

🌐 Despliegue API
Ejecutar local
docker run -p 8000:8000 churn-model-api


Endpoint:

POST /predict


Entrada JSON:

{
  "MonthlyCharges": 20,
  "gender": "Female",
  "tenure": 10
}

🐳 Docker
docker build -t churn-model-api .
docker run -p 8000:8000 churn-model-api

✅ Buenas Prácticas

✅ Uso de entornos virtuales
✅ Modularización
✅ Control de configuración
✅ Versionado
✅ Modelos exportables

📄 Licencia

MIT License

✨ Autor

Miguel Gallego Álvarez
Machine Learning & Data Science

🔗 GitHub: https://github.com/MiguelGalleg05 
