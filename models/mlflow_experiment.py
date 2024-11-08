# mlflow_experiment.py
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import yaml

# Load configuration for model parameters
with open('configs/model_config.yaml', 'r') as f:
    model_config = yaml.safe_load(f)

# Load and preprocess data
data = pd.read_csv('data/processed/processed_data.csv')
X = data.drop('failure', axis=1, errors='ignore')
y = data['failure']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(**model_config['model']['parameters'])
model.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# MLflow experiment logging
mlflow.set_experiment("IoT Predictive Maintenance")
with mlflow.start_run():
    # Log model parameters
    mlflow.log_params(model_config['model']['parameters'])
    mlflow.log_metric("accuracy", accuracy)

    # Log the model itself
    mlflow.sklearn.log_model(model, "model")

    print(f"Logged experiment with accuracy: {accuracy}")

