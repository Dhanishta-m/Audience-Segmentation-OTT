import os
import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# -------------------------
# Load Users Dataset
# -------------------------
users_df = pd.read_csv("dataset/users.csv")

# -------------------------
# Encode Genre
# -------------------------
encoder = LabelEncoder()
users_df["GenreEncoded"] = encoder.fit_transform(users_df["PreferredGenre"])

# -------------------------
# Select Features
# -------------------------
X = users_df[
    [
        "Age",
        "GenreEncoded",
        "WatchHours",
        "LoginPerWeek",
        "CompletionRate"
    ]
]

# -------------------------
# Scale Data
# -------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------
# Train KMeans
# -------------------------
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

users_df["Cluster"] = kmeans.fit_predict(X_scaled)

# -------------------------
# Save Model
# -------------------------
joblib.dump(kmeans, "models/kmeans.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(encoder, "models/label_encoder.pkl")

print("✅ Model Trained Successfully")

print("\nCluster Count:")
print(users_df["Cluster"].value_counts())

print("\nFirst 10 Users:")
print(users_df.head(10))