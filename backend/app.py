from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

from recommendation import get_recommendation

app = Flask(__name__)
CORS(app)

# Load trained model (fixed path)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "kmeans.pkl")

model = joblib.load(MODEL_PATH)


# Genre encoding
genre_mapping = {
    "Action": 0,
    "Comedy": 1,
    "Drama": 3,
    "Horror": 4,
    "Romance": 6,
    "Sci-Fi": 7
}


# Home Route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "OTT Audience Segmentation API Running"
    })


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        print("Received Data:", data)

        genre = genre_mapping.get(
            data.get("PreferredGenre"),
            0
        )

        user_data = np.array([[
            int(data["Age"]),
            genre,
            int(data["WatchHours"]),
            int(data["LoginPerWeek"]),
            int(data["CompletionRate"])
        ]])

        # Predict cluster
        cluster = int(model.predict(user_data)[0])

        # Get recommendation
        result = get_recommendation(cluster)

        return jsonify({
            "cluster": cluster,
            "segment": result["segment"],
            "recommendations": result["content"]
        })

    except Exception as e:
        import traceback
        traceback.print_exc()

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )