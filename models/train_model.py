# models/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
data = pd.read_csv('data/processed/sensor_data.csv')
X = data.drop("failure", axis=1, errors="ignore")
y = data.get("failure", pd.Series([0]*len(data)))  # Example target column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'models/failure_prediction_model.pkl')
