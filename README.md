# Examen Final – Predicción de Riesgo de Diabetes 

Este proyecto implementa una arquitectura básica de MLOps usando FastAPI, entrenamiento automático con DVC, y un modelo predictivo de riesgo de diabetes basado en características del paciente.

---

# Estructura del Proyecto

- `main.py` → API con FastAPI para predicción de riesgo
- `train.py` → Script de entrenamiento del modelo
- `modelo_entrenado.pkl` → Modelo entrenado guardado con `joblib`
- `datos_diabetes.csv` → Dataset usado para el entrenamiento
- `requirements.txt` → Lista de dependencias
- `dvc.yaml` y `.dvc/` → Pipeline de entrenamiento automatizado

---

# Tecnologías Utilizadas

- **FastAPI** → Framework para API REST
- **scikit-learn** → Entrenamiento del modelo de clasificación
- **joblib** → Serialización del modelo
- **DVC** → Automatización del reentrenamiento
- *(MongoDB Atlas fue implementado pero desactivado por problemas de red en la ejecución final)*

# ¿Cómo ejecutar el proyecto localmente?
1. Clonar el repositorio

```bash
git clone https://github.com/Roselind26/Examen_Final-.git
cd Examen_Final-

