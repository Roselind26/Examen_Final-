from fastapi import FastAPI
import joblib
from pymongo import MongoClient

# Inicializar la API
app = FastAPI(
    title="Predicción de Riesgo de Diabetes",
    description="API para predecir riesgo de diabetes con conexión a MongoDB Atlas",
    version="1.0"
)

# Cargar el modelo entrenado
model = joblib.load("modelo_entrenado.pkl")

# Conexión a MongoDB Atlas (URI corregido)
client = MongoClient("mongodb+srv://roselind_user:Rvd2021135152@cluster0.vls2u6y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Base de datos y colección
db = client["diabetes_db"]
pacientes = db["pacientes"]

# Endpoint para predecir el riesgo de diabetes
@app.post("/predict")
def predict(data: dict):
    input_data = [[data["edad"], data["glucosa"], data["bmi"]]]
    prediction = model.predict(input_data)
    resultado = int(prediction[0])

    # Guardar datos y resultado en MongoDB
    pacientes.insert_one({
        "datos": data,
        "riesgo": resultado
    })

    return {"riesgo_diabetes": resultado}

# (Opcional) Endpoint para listar pacientes registrados
@app.get("/pacientes")
def listar_pacientes():
    return list(pacientes.find({}, {"_id": 0}))
