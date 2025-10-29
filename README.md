  # 🧠 Proyecto de Machine Learning  
  > Pipeline de modelado supervisado con enfoque en clasificación

  ---

  ## 📌 Descripción

  Este proyecto implementa un pipeline completo de Machine Learning para resolver un problema supervisado de clasificación.  

  Incluye:
  - Carga y validación de datos
  - Análisis Exploratorio (EDA)
  - Feature Engineering
  - Entrenamiento de modelos
  - Evaluación
  - Guardado de artefactos
  - Base para despliegue y monitoreo

  ---

 
  ## 📂 Estructura del Proyecto
  
   
  
  ```
  PROYECTO_MACHINE_LEARNING/              # Raíz del proyecto
  │
  ├── steps_pipeline/                     # Flujo principal del pipeline
  │   └── src/                            # Código y notebooks del pipeline
  │       ├── carga_datos.ipynb           # Carga inicial de datos y limpieza básica
  │       ├── compresion_eda.ipynb        # Análisis exploratorio (EDA)
  │       ├── ft_engineering.py           # Feature engineering (scaling, encoding, selección)
  │       ├── heuristic_model.py          # Modelo base sencillo (baseline)
  │       ├── model_training.ipynb        # Entrenamiento de modelos
  │       ├── model_deploy.ipynb          # Ejemplo de despliegue (API/serving)
  │       ├── model_evaluation.ipynb      # Evaluación de métricas
  │       └── model_monitoring.ipynb      # Monitoreo y detección de drift
  │
  ├── config.json                         # Configuración global del pipeline
  ├── base_de_datos.csv                   # Dataset original de ejemplo
  ├── requirements.txt                    # Dependencias del proyecto
  ├── .gitignore                          # Archivos/carpetas a ignorar por Git
  ├── README.md                           # Documentación principal del proyecto
  └── set_up.bat                          # Script para preparar el entorno en Windows
  ```


---

## ✅ Funcionalidades Principales

✔ Gestión de configuración mediante `config.json`  
✔ Carga de datos centralizada  
✔ Limpieza y validación automática  
✔ EDA completo  
✔ Feature Engineering programable  
✔ Entrenamiento de modelos tradicionales  
✔ Evaluación con múltiples métricas  
✔ Exportación de modelos  
✔ Scripts base para despliegue y monitoreo  

---

## 🧩 Configuración (`config.json`)

Este archivo controla los parámetros principales del pipeline:  
- Paths de entrada/salida  
- Columna objetivo  
- Proporción de datos train/test  
- Tipo de modelo y parámetros  
- Métricas de evaluación  

```json
{
  "data": {
    "input_path": "base_de_datos.csv",
    "clean_path": "data_limpia.csv",
    "target_column": "target",
    "test_size": 0.2,
    "random_state": 42
  },
  "preprocessing": {
    "scale_numeric": true,
    "impute_missing": true,
    "encode_categorical": true
  },
  "model": {
    "type": "RandomForestClassifier",
    "params": {
      "n_estimators": 200,
      "max_depth": null,
      "min_samples_split": 2,
      "min_samples_leaf": 1
    }
  },
  "evaluation": {
    "metrics": [
      "accuracy",
      "precision",
      "recall",
      "f1",
      "roc_auc"
    ]
  },
  "output": {
    "model_path": "modelo_rf.pkl",
    "reports_path": "reports/"
  }
}

```

## ⚙ Instalación del entorno

### ✅ Opción automática (Windows)
Ejecutar:
```bash
set_up.bat
```

### ✅ Opción manual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## 📦 Dependencias Principales

Las principales librerías se encuentran en `requirements.txt`:

- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn
- xgboost
- lightgbm
- imbalanced-learn
- statsmodels
- joblib
- jupyter

---

## 🚀 Ejecución del Pipeline

1️⃣ **Carga / limpieza de datos**  
📄 `steps_pipeline/src/carga_datos.ipynb`

2️⃣ **EDA completo**  
📄 `steps_pipeline/src/compresion_eda.ipynb`

3️⃣ **Entrenamiento del modelo**  
📄 `steps_pipeline/src/model_training.ipynb`

4️⃣ **Evaluación del modelo**  
📄 `steps_pipeline/src/model_evaluation.ipynb`

5️⃣ **Exportar modelo entrenado**  
📄 `modelo_rf.pkl`

---

## 📊 Métricas disponibles

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

---

## 🧩 Feature Engineering

📄 `steps_pipeline/src/ft_engineering.py`  
Incluye funciones para:
- Scaling
- Encoding
- Selección de variables

---

## 🌐 Despliegue y Monitoreo

- Despliegue del modelo  
📄 `steps_pipeline/src/model_deploy.ipynb`

- Monitoreo de performance / drift  
📄 `steps_pipeline/src/model_monitoring.ipynb`

---

## ✅ Buenas Prácticas

- Configuración global → `config.json`
- Versionado → Git
- No subir archivos pesados → `.gitignore`
- Uso de entornos virtuales
- Modularización de funciones
- Guardado de modelos con `joblib`

---

## 📄 Licencia

Este proyecto se distribuye bajo licencia **MIT**.

---

## ✨ Autor

**Miguel Gallego Álvarez**  
Machine Learning & Data Science  
LinkedIn:  
GitHub:  
