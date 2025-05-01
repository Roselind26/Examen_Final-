from fastapi import FastAPI
import joblib
from pymongo import MongoClient

app = FastAPI()
model = joblib.load("modelo_entrenado.pkl")

# Conexión con tu URI (sin espacios ni errores de formato)
client = MongoClient("mongodb+srv://roselind_user:Rvd2021135152.@cluster0.vls2u6y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["diabetes_db"]
pacientes = db["pacientes"]

@app.post("/predict")
def predict(data: dict):
    input_data = [[data["edad"], data["glucosa"], data["bmi"]]]
    prediction = model.predict(input_data)
    resultado = int(prediction[0])

    # Guardar en MongoDB
    pacientes.insert_one({
        "datos": data,
        "riesgo": resultado
    })

    return {"riesgo_diabetes": resultado}


