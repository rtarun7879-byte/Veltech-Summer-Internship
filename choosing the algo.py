import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    ConfusionMatrixDisplay
)

# Load Dataset

df = pd.read_csv("crop production.csv")

print("Dataset Shape")
print(df.shape)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

# Remove Missing Values

df.dropna(inplace=True)

# Encode Text Columns

encoders = {}

for col in df.select_dtypes(include="object").columns:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col].astype(str))
    encoders[col] = encoder

print("\nDataset After Cleaning")
print(df.head())

# Features and Target

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Shape")
print(X_train.shape)

print("\nTesting Shape")
print(X_test.shape)

# Logistic Regression

lr_model = LogisticRegression(max_iter=1000)

lr_model.fit(X_train, y_train)

y_pred_lr = lr_model.predict(X_test)

# Decision Tree

dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

y_pred_dt = dt_model.predict(X_test)

# Random Forest

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

# First 10 Predictions

print("\nFirst 10 Predictions")

comparison = pd.DataFrame({
    "Actual": y_test.values[:10],
    "Predicted": y_pred_rf[:10]
})

print(comparison)

# Prediction Probabilities

print("\nPrediction Probabilities")

try:
    probs = rf_model.predict_proba(X_test)
    print(probs[:10])
except:
    print("Probability output unavailable")

# Metrics Table

results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],

    "Accuracy": [
        accuracy_score(y_test, y_pred_lr),
        accuracy_score(y_test, y_pred_dt),
        accuracy_score(y_test, y_pred_rf)
    ],

    "Precision": [
        precision_score(y_test, y_pred_lr, average="weighted"),
        precision_score(y_test, y_pred_dt, average="weighted"),
        precision_score(y_test, y_pred_rf, average="weighted")
    ],

    "Recall": [
        recall_score(y_test, y_pred_lr, average="weighted"),
        recall_score(y_test, y_pred_dt, average="weighted"),
        recall_score(y_test, y_pred_rf, average="weighted")
    ],

    "F1 Score": [
        f1_score(y_test, y_pred_lr, average="weighted"),
        f1_score(y_test, y_pred_dt, average="weighted"),
        f1_score(y_test, y_pred_rf, average="weighted")
    ]
})

print("\nModel Comparison")
print(results)

# Best Model

best_model = results.loc[
    results["Accuracy"].idxmax()
]

print("\nBest Model")
print(best_model)

# Classification Report

print("\nRandom Forest Classification Report")

print(
    classification_report(
        y_test,
        y_pred_rf
    )
)

# Chart 1

plt.figure(figsize=(8,5))

plt.bar(
    results["Model"],
    results["Accuracy"]
)

plt.title("Algorithm Accuracy Comparison")
plt.xlabel("Algorithm")
plt.ylabel("Accuracy")

plt.tight_layout()
plt.show()

# Chart 2

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

plt.figure(figsize=(10,6))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.title("Feature Importance")

plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

# Chart 3

fig, ax = plt.subplots(figsize=(6,6))

ConfusionMatrixDisplay.from_estimator(
    rf_model,
    X_test,
    y_test,
    ax=ax
)

plt.title("Random Forest Confusion Matrix")

plt.show()

# Chart 4

metric_chart = results.set_index("Model")

metric_chart[
    [
        "Precision",
        "Recall",
        "F1 Score"
    ]
].plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Precision Recall F1 Comparison")

plt.ylabel("Score")

plt.tight_layout()

plt.show()

# Save Model

joblib.dump(
    rf_model,
    "first_model.pkl"
)

# Save Encoders

for name, encoder in encoders.items():
    joblib.dump(
        encoder,
        f"{name}_encoder.pkl"
    )

# Save CSV

results.to_csv(
    "algorithm_comparison.csv",
    index=False
)

print("\nPrediction Count")
print(len(y_pred_rf))
print(len(y_test))

print("\nFiles Saved Successfully")
