# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load sample dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
X = df.drop("species", axis=1)
y = df["species"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("model/trained_model.pkl", "wb") as f:
    pickle.dump(model, f)
