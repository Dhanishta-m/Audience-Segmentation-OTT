import streamlit as st
import joblib
import numpy as np
import os

from backend.recommendation import get_recommendation


# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "backend",
    "models",
    "kmeans.pkl"
)

model = joblib.load(MODEL_PATH)


genre_mapping = {
    "Action": 0,
    "Comedy": 1,
    "Drama": 3,
    "Horror": 4,
    "Romance": 6,
    "Sci-Fi": 7
}


st.title("🎬 AI OTT Audience Segmentation")


age = st.number_input("Age", 10, 100)
genre = st.selectbox(
    "Preferred Genre",
    list(genre_mapping.keys())
)
watch_hours = st.number_input("Watch Hours")
login = st.number_input("Login Per Week")
completion = st.number_input("Completion Rate")


if st.button("Predict Segment"):

    user_data = np.array([[
        age,
        genre_mapping[genre],
        watch_hours,
        login,
        completion
    ]])


    cluster = int(model.predict(user_data)[0])

    result = get_recommendation(cluster)

    st.success(
        f"Audience Segment: {result['segment']}"
    )

    st.write(
        "Recommended Content:"
    )

    for item in result["content"]:
        st.write("•", item)