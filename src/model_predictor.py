
import joblib
import numpy as np

def load_model(model_path):
    model = joblib.load(model_path)
    print(f"[INFO] Loaded model from {model_path}")
    return model

def predict(model, input_data):
    prediction = model.predict(np.array(input_data).reshape(1, -1))
    return prediction[0]
