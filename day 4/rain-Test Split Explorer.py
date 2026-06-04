# Import pandas library
import pandas as pd

# Import train_test_split
from sklearn.model_selection import train_test_split

# ==========================
# LOAD EXCEL DATASET
# ==========================

data = pd.read_csv(r"D:\veltech summerintenship\day 4\crop production.csv")# Display first 5 rows
print("First 5 Rows")
print(data.head())

# Display dataset shape
print("\nDataset Shape")
print(data.shape)

# ==========================
# FEATURES
# ==========================

X = data[[
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph",
    "rainfall"
]]

# ==========================
# TARGET COLUMN
# ==========================

y = data["label"]

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
# OUTPUT
# ==========================

print("\nTraining Features Shape")
print(X_train.shape)

print("\nTesting Features Shape")
print(X_test.shape)

print("\nTraining Labels Shape")
print(y_train.shape)

print("\nTesting Labels Shape")
print(y_test.shape)

print("\nTraining Data Sample")
print(X_train.head())

print("\nTesting Data Sample")
print(X_test.head())

print("\nTask 3 Completed Successfully")
