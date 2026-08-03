import pandas as pd
import random

genres = [
    "Action", "Comedy", "Drama", "Horror",
    "Romance", "Sci-Fi", "Documentary", "Kids"
]

users = []

for i in range(1, 10001):
    users.append({
        "UserID": i,
        "Age": random.randint(18, 60),
        "PreferredGenre": random.choice(genres),
        "WatchHours": random.randint(5, 120),
        "LoginPerWeek": random.randint(1, 7),
        "CompletionRate": random.randint(40, 100)
    })

df = pd.DataFrame(users)
df.to_csv("dataset/users.csv", index=False)

print("✅ users.csv created successfully!")
print(df.head())