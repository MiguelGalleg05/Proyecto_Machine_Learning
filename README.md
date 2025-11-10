# 🧠 Proyecto de Machine Learning  
> Pipeline modular para un problema supervisado de clasificación (Churn)

---

## 📌 Descripción

Este proyecto implementa un pipeline completo de Machine Learning para resolver un problema supervisado tipo **clasificación**, desde la carga de datos hasta el despliegue del modelo.

El flujo incluye:

- Carga y validación de datos
- Análisis Exploratorio (EDA)
- Feature Engineering
- Entrenamiento de múltiples modelos
- Evaluación comparativa
- Selección y guardado del mejor modelo
- Monitoreo (Data Drift)
- Exposición vía API
- Contenerización con Docker

---

## 🎯 Objetivos

✅ Desarrollar un pipeline ML modular  
✅ Entrenar múltiples modelos y seleccionar el mejor  
✅ Realizar monitoreo periódico  
✅ Exponer el modelo mediante API  
✅ Desplegar como contenedor Docker  

---

## 📂 Estructura del Proyecto
```bash
Proyecto_Machine_Learning/
│
├── data/                              # Datos
│   ├── Base_de_datos.csv              # Dataset original
│   └── monitoring/
│       └── data_drift_report.csv      # Resultados medición drift
│
├── mlops_pipeline/
│   └── src/
│       ├── Cargar_datos.ipynb         # Carga inicial
│       ├── compresion_eda.ipynb       # EDA completo
│       ├── ft_engineering.py          # Feature Engineering
│       ├── model_training.ipynb       # Entrenamiento
│       ├── model_training_evaluation.py # Evaluación
│       ├── model_evaluation.ipynb     # Métricas
│       ├── model_monitoring.ipynb     # Monitoreo
│       ├── model_monitoring.py        # Data drift
│       ├── model_deploy.ipynb         # Despliegue
│       ├── model_deploy.py            # API
│       └── utils/                     # Módulos auxiliares
│
├── models/
│   └── best_model.pkl                 # Mejor modelo
│
├── app/
│   └── streamlit_app.py               # UI Monitoreo
│
├── Dockerfile
├── requirements.txt
├── config.json
├── set_up.bat
└── README.md
```
## ✅ Funcionalidades Principales

✔ Gestión de configuración mediante `config.json`  
✔ Carga de datos centralizada  
✔ Limpieza y validación automática  
✔ EDA completo  
✔ Feature Engineering programable  
✔ Entrenamiento de múltiples modelos  
✔ Evaluación con múltiples métricas  
✔ Exportación del mejor modelo  
✔ Monitoreo de Data Drift  
✔ Exposición de API con FastAPI  
✔ Contenerización Docker  


---

## ⚙ Configuración (`config.json`)

```json
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
```
---

## 🧰 Instalación del entorno

✅ **Crear entorno virtual**
python -m venv venv

✅ Activar entorno
## Windows
venv\Scripts\activate

## MacOS / Linux
source venv/bin/activate

✅ Instalar dependencias
pip install -r requirements.txt


---

## 🚀 Ejecución del Pipeline

### 🔹 1 — Carga y Limpieza
📄 `Cargar_datos.ipynb`

Realiza:
- Lectura de dataset
- Identificación de nulos
- Normalización de valores
- Corrección de tipos de datos


### 🔹 2 — Análisis Exploratorio (EDA)
📄 `compresion_eda.ipynb`

Incluye:
- `describe()`
- Distribución de variables
- Detección de outliers
- Matrices de correlación
- Relación con la variable objetivo


### 🔹 3 — Ingeniería de Características
📄 `ft_engineering.py`

Incluye:
- Encoding
- Escalado
- Imputación
- Separación Train/Test


### 🔹 4 — Entrenamiento del Modelo
📄 `model_training.ipynb`

Modelos probados:
- Logistic Regression
- RandomForest
- XGBoost
- LightGBM


### 🔹 5 — Evaluación
📄 `model_training_evaluation.py`

✔ Se compara el rendimiento  
✔ Se selecciona el mejor modelo  
✔ Se guarda en:




### 🔹 6 — Monitoreo (Data Drift)
📄 `model_monitoring.py`

Métricas calculadas:
- KS Test
- PSI
- Jensen–Shannon
- Chi²

Salida:

- data/monitoring/data_drift_report.csv


---

## 📊 Métricas disponibles

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Population Stability Index (PSI)
- Kolmogorov–Smirnov (KS)
- Chi²
- Jensen–Shannon

---

## 🌐 Despliegue API

Ejecutar API localmente:

```bash
uvicorn mlops_pipeline.src.model_deploy:app --reload
```
### ✅ Endpoint disponible

/predict
Soporta:
Predicciones individuales
Predicciones por lote
Formato JSON

---
## 🐳 Docker

✅ **Construir imagen**
```
docker build -t churn-model-api .
```
✅ Ejecutar contenedor


docker run -p 8000:8000 churn-model-api
🔗 Acceso por defecto

http://localhost:8000

---

## 🛡️ SonarCloud — Calidad del Código

Este proyecto está integrado con **SonarCloud** para analizar y monitorear la calidad, seguridad y mantenibilidad del código fuente.

🔍 **Análisis realizados:**
- ✅ Calidad del código (mantenibilidad)
  - Complejidad ciclomática
  - Código duplicado
  - Funciones extensas o complejas
  - Code smells
- ✅ Seguridad
  - Vulnerabilidades
  - Dependencias inseguras
  - Exposición de datos sensibles
- ⚠️ Cobertura de pruebas
  - (Disponible si se integran pruebas unitarias)
- ✅ Estilo e integridad
  - Nombres consistentes
  - Indentación adecuada
  - Buenas prácticas generales

🔗 **Dashboard del Proyecto en SonarCloud:**  
https://sonarcloud.io/project/overview?id=MiguelGalleg05_Proyecto_Machine_Learning

✅ *El proyecto fue analizado correctamente mediante SonarCloud.  
No se detectan problemas críticos de seguridad ni mantenibilidad.*

<img width="1919" height="968" alt="image" src="https://github.com/user-attachments/assets/1dd60c1e-00e8-4920-a93c-345dd4bc627d" />

<img width="1919" height="968" alt="image" src="https://github.com/user-attachments/assets/f405c719-f4e6-432f-be38-fa68f13bad1c" />


---

## ✅ Buenas Prácticas

- Uso de entornos virtuales
- Modularización del código
- Versionado con Git
- No subir modelos o datasets pesados
- Configuración centralizada (`config.json`)
- Separación clara de etapas del pipeline


Este proyecto está bajo licencia **MIT**.

## ✨ Autor

**Miguel Gallego Álvarez**  
Machine Learning & Data Science  

🔗 GitHub: https://github.com/MiguelGalleg05
