
import streamlit as st
from src.model_predictor import load_model, predict

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GlucoInsight | ML Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #0b1120;
    color: #e5e7eb;
}

[data-testid="stSidebar"] {
    background: #111b2e;
    border-right: 1px solid #243249;
}

[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

.hero {
    background: linear-gradient(120deg, #14263d, #123c45);
    padding: 35px;
    border-radius: 20px;
    border: 1px solid #28535b;
    margin-bottom: 25px;
}

.hero h1 {
    color: #f8fafc;
    font-size: 38px;
    margin-bottom: 8px;
    font-weight: 800;
}

.hero p {
    color: #a9c5ce;
    font-size: 15px;
}

.section-title {
    color: #f1f5f9;
    font-size: 22px;
    font-weight: 700;
    margin: 25px 0 15px 0;
}

.info-card {
    background: #142136;
    border: 1px solid #293a53;
    padding: 20px;
    border-radius: 15px;
    min-height: 115px;
}

.info-card h3 {
    color: #7dd3c7;
    font-size: 14px;
    margin: 0 0 10px 0;
}

.info-card p {
    color: #f8fafc;
    font-size: 19px;
    font-weight: 700;
    margin: 0;
}

.result-card {
    background: #142136;
    border: 1px solid #31516a;
    border-radius: 16px;
    padding: 25px;
    margin-top: 20px;
}

.result-card h2 {
    color: #7dd3c7;
}

.small-muted {
    color: #94a3b8;
    font-size: 13px;
}

.stButton > button {
    background: linear-gradient(90deg, #0d9488, #0f766e);
    color: white;
    border: none;
    border-radius: 10px;
    height: 48px;
    font-weight: 700;
    width: 100%;
}

.stButton > button:hover {
    background: #14b8a6;
    color: white;
    border: none;
}

div[data-testid="stForm"] {
    background: #111b2e;
    border: 1px solid #293a53;
    border-radius: 16px;
    padding: 25px;
}

label {
    color: #cbd5e1 !important;
}

hr {
    border-color: #293a53;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 🧬 GlucoInsight")
    st.caption("MACHINE LEARNING DASHBOARD")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        ["Dashboard", "About Project"]
    )

    st.divider()

    st.markdown("### Project Details")
    st.caption("Model: Random Forest")
    st.caption("Task: Binary Classification")
    st.caption("Framework: Streamlit")

    st.divider()

    st.caption("Educational ML Demonstration")


# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>Diabetes Prediction Dashboard</h1>
        <p>
        Machine learning based educational demonstration
        using patient health parameters.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # INFORMATION CARDS
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="info-card">
            <h3>MODEL</h3>
            <p>Random Forest</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">
            <h3>INPUT FEATURES</h3>
            <p>8 Parameters</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="info-card">
            <h3>APPLICATION</h3>
            <p>Health ML Demo</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Patient Parameters</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter the values below to explore the model's classification output."
    )

    # ---------------- INPUT FORM ----------------
    with st.form("prediction_form"):

        left, right = st.columns(2)

        with left:
            st.markdown("### 🩺 Basic Health Metrics")

            glucose = st.slider(
                "Glucose Level",
                0, 200, 120
            )

            bp = st.slider(
                "Blood Pressure",
                0, 140, 70
            )

            bmi = st.slider(
                "BMI",
                0.0, 70.0, 25.0
            )

            age = st.slider(
                "Age",
                10, 100, 35
            )

        with right:
            st.markdown("### 📊 Additional Parameters")

            insulin = st.slider(
                "Insulin",
                0, 300, 90
            )

            preg = st.slider(
                "Pregnancies",
                0, 15, 1
            )

            skin = st.slider(
                "Skin Thickness",
                0, 99, 20
            )

            dpf = st.slider(
                "Diabetes Pedigree Function",
                0.0, 2.5, 0.5
            )

        st.markdown("---")

        submitted = st.form_submit_button(
            "🚀 Run Model Assessment",
            use_container_width=True
        )

    # ---------------- PREDICTION ----------------
    if submitted:

        input_data = [
            preg,
            glucose,
            bp,
            skin,
            insulin,
            bmi,
            dpf,
            age
        ]

        try:
            model = load_model(
                "models/random_forest_model.pkl"
            )

            result = predict(model, input_data)

            st.markdown(
                '<div class="section-title">Model Output</div>',
                unsafe_allow_html=True
            )

            if result == 1:
                st.warning(
                    "Model output: Class 1"
                )
                st.markdown("""
                <div class="result-card">
                    <h2>Classification: 1</h2>
                    <p>
                    The model assigned this input to class 1.
                    </p>
                    <p class="small-muted">
                    This is a model classification, not a medical diagnosis.
                    </p>
                </div>
                """, unsafe_allow_html=True)

            else:
                st.success(
                    "Model output: Class 0"
                )
                st.markdown("""
                <div class="result-card">
                    <h2>Classification: 0</h2>
                    <p>
                    The model assigned this input to class 0.
                    </p>
                    <p class="small-muted">
                    This is a model classification, not a medical diagnosis.
                    </p>
                </div>
                """, unsafe_allow_html=True)

        except FileNotFoundError:
            st.error(
                "Model file not found. Check the models folder."
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")


# ---------------- ABOUT PROJECT ----------------
elif page == "About Project":

    st.markdown("""
    <div class="hero">
        <h1>About GlucoInsight</h1>
        <p>
        Understanding machine learning through a
        diabetes classification demonstration.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Project Overview")

    st.write("""
    GlucoInsight is a machine learning project that demonstrates
    how a Random Forest classification model processes numerical
    health-related inputs and produces a binary classification.
    """)

    st.markdown("### Technology Stack")

    t1, t2, t3 = st.columns(3)

    with t1:
        st.markdown("""
        <div class="info-card">
            <h3>LANGUAGE</h3>
            <p>Python</p>
        </div>
        """, unsafe_allow_html=True)

    with t2:
        st.markdown("""
        <div class="info-card">
            <h3>ML LIBRARY</h3>
            <p>Scikit-learn</p>
        </div>
        """, unsafe_allow_html=True)

    with t3:
        st.markdown("""
        <div class="info-card">
            <h3>WEB FRAMEWORK</h3>
            <p>Streamlit</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Important Disclaimer")

    st.info("""
    This project is intended only for educational and
    demonstration purposes. It is not clinically validated,
    must not be used for medical decisions, and does not
    replace professional medical advice.
    """)
