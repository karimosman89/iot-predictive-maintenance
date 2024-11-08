# models/inference.py
import joblib
import pandas as pd

model = joblib.load('models/failure_prediction_model.pkl')

def predict_failure(sensor_data):
    df = pd.DataFrame([sensor_data])
    prediction = model.predict(df)
    return prediction[0]

# Test with a sample data
sample_data = {"temperature": 60, "vibration": 3.5, "pressure": 150}
print(f"Prediction: {predict_failure(sample_data)}")


