import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Cargar el CSV real
df = pd.read_csv("datos_diabetes.csv")

# Seleccionar solo las variables que usamos en la API
X = df[["Age", "Glucose", "BMI"]]
y = df["Outcome"]

# Entrenar el modelo
X_train, _, y_train, _ = train_test_split(X, y)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(model, "modelo_entrenado.pkl")
