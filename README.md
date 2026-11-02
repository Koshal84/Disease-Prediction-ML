# 🧬 GlucoInsight — Diabetes Prediction Using Machine Learning

GlucoInsight is a machine learning web application that demonstrates diabetes-related binary classification using a Random Forest model. Users can enter health-related parameters through an interactive Streamlit dashboard and view the model's classification output.

> **Disclaimer:** This project is for educational and demonstration purposes only. It is not clinically validated, does not provide a medical diagnosis, and must not be used to make healthcare decisions.

## ✨ Features

- Interactive dashboard built with Streamlit.
- Eight numerical input parameters.
- Random Forest classification model.
- Organized patient-input form.
- Instant model output.
- Dedicated project information page.
- Custom dark-themed user interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning |
| Joblib | Model loading |

## 📊 Input Features

The application accepts the following eight parameters:

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

The trained model returns a binary class label: `0` or `1`.

These labels represent the model's output classes, not a confirmed health status.

## 📁 Project Structure

```text
disease_predictor_final/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── data/
│   └── raw/
│       └── diabetes_sample.csv
│
├── models/
│   └── random_forest_model.pkl
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── model_predictor.py
│   ├── model_trainer.py
│   └── utils.py
│
└── tests/
```

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Disease-Prediction-ML.git
```

### 2. Navigate to the project directory

```bash
cd Disease-Prediction-ML
```

### 3. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application should open in your browser at:

`http://localhost:8501`

## 🧠 Machine Learning Workflow

The project is organized around a simple machine learning workflow:

1. Load the available dataset.
2. Prepare and preprocess the data.
3. Train a Random Forest classification model.
4. Save the trained model.
5. Load the saved model in the Streamlit application.
6. Accept user inputs and generate a classification output.

## ⚠️ Limitations

- The included sample dataset is small and is not sufficient to establish model reliability.
- The application has not been clinically validated.
- Predictions depend on the quality and representativeness of the training data.
- Model outputs should not be interpreted as medical advice or diagnoses.

## 🔮 Future Improvements

- Train and evaluate the model using a larger, properly documented dataset.
- Add model evaluation metrics such as precision, recall, F1-score and ROC-AUC.
- Add visualizations for exploratory data analysis.
- Implement input validation and improved error handling.
- Add explainability using feature importance or SHAP.
- Add automated unit and integration tests.

## 👨‍💻 Author

**Your Name**

B.Tech — Computer Science and Engineering

GitHub: [Your GitHub Profile](https://github.com/YOUR_USERNAME)

---

⭐ If you find this project useful, consider giving the repository a star.

**Built as a machine learning and Python application development project.**