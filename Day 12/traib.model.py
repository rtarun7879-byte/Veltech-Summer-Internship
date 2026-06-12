import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

print("Current Folder:")
print(os.getcwd())

df = pd.read_csv(r"D:\veltech summerintenship\day 6\crop production.csv")

X = df[['N','P','K','temperature','humidity','ph','rainfall']]
y = df['label']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

model = RandomForestClassifier()

model.fit(X, y_encoded)

joblib.dump(model, "model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("Model Saved Successfully")