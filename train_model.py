import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import os

# Load dataset
csv_path = os.path.join("data", "raw", "diabetes_sample.csv")
df = pd.read_csv(csv_path)

# Define features and label
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Define pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train model
pipeline.fit(X, y)

# Save trained model
model_dir = "models"
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, "random_forest_model.pkl")
joblib.dump(pipeline, model_path)

print(f"✅ Model trained and saved to {model_path}")
