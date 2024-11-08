# preprocess_data.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
import yaml

# Load preprocessing configuration
with open('configs/model_config.yaml', 'r') as f:
    model_config = yaml.safe_load(f)

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess(df):
    # Handle missing values
    df = df.dropna()
    
    # Feature scaling
    scaler = StandardScaler()
    features = ["temperature", "vibration", "pressure"]
    df[features] = scaler.fit_transform(df[features])

    # Label encoding (for categorical variables, if needed)
    # df['some_categorical_feature'] = df['some_categorical_feature'].astype('category').cat.codes

    return df

if __name__ == "__main__":
    data = load_data('data/raw_data.csv')
    processed_data = preprocess(data)
    processed_data.to_csv('data/processed/processed_data.csv', index=False)
    print("Data preprocessing complete.")

