import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Dataset de ejemplo (reemplaza con tu archivo real)
df = pd.read_csv("datos_diabetes.csv")

X = df[["edad", "glucosa", "bmi"]]
y = df["diabetes"]

X_train, _, y_train, _ = train_test_split(X, y)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

joblib.dump(clf, "modelo_entrenado.pkl")
