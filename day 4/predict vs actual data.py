import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ==========================
# LOAD DATASET
# ==========================

data = pd.read_csv(r"D:\veltech summerintenship\day 4\crop production.csv")

print("Dataset Loaded Successfully")

print(data.head())

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
# PREDICT
# ==========================

y_pred = model.predict(X_test)

# ==========================
# ACTUAL VS PREDICTED PLOT
# ==========================

plt.figure(figsize=(8,6))

plt.scatter(
    y_test,
    y_pred
)

plt.title("Actual vs Predicted Rainfall")

plt.xlabel("Actual Rainfall")

plt.ylabel("Predicted Rainfall")

plt.grid(True)

plt.savefig("Actual_vs_Predicted.png")

plt.show()

# ==========================
# DISPLAY RESULTS
# ==========================

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\nComparison Table")

print(comparison.head(10))

print("\nTask 6 Completed Successfully")
