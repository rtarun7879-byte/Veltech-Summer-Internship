import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import pickle

# ==========================
# LOAD DATASET
# ==========================

data = pd.read_csv(r"D:\veltech summerintenship\day 4\crop production.csv")

# ==========================
# FEATURES
# ==========================

X = data[[
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph"
]]

# ==========================
# TARGET
# ==========================

y = data["rainfall"]

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# TRAIN MODEL
# ==========================

model = LinearRegression()

model.fit(X_train, y_train)

# ==========================
# SAVE MODEL
# ==========================

with open("crop_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully")

# ==========================
# LOAD MODEL
# ==========================

with open("crop_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

print("Model Loaded Successfully")

print("Task 7 Completed Successfully")
