
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Loaded data from {file_path} with shape {df.shape}")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")
        return None

def preprocess_data(df, label_column):
    df_clean = df.dropna()
    X = df_clean.drop(label_column, axis=1)
    y = df_clean[label_column]
    print(f"[INFO] Preprocessed data. Features shape: {X.shape}, Labels shape: {y.shape}")
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    print(f"[INFO] Data split into train ({X_train.shape[0]}) and test ({X_test.shape[0]}) samples.")
    return X_train, X_test, y_train, y_test
