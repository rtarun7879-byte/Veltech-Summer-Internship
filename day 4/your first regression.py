import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load Dataset

data = pd.read_csv(r"D:\veltech summerintenship\day 4\crop production.csv")

# Display first 5 rows

print("First 5 Rows")
print(data.head())

# Display column names

print("\nColumn Names")
print(data.columns)

# Features

X = data[[
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "ph"
]]

# Target

y = data["rainfall"]

# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Regression Model

model = LinearRegression()

# Train Model

model.fit(X_train, y_train)

# Predict Values

predictions = model.predict(X_test)

# Output

print("\nPredicted Rainfall Values")
print(predictions[:10])

print("\nActual Rainfall Values")
print(y_test.head(10))

print("\nTask 4 Completed Successfully")
