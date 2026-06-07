# Import libraries

import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Load dataset

df = pd.read_csv("crop production.csv")

print("Dataset Shape")
print(df.shape)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

# Clean data

df.dropna(inplace=True)

encoders = {}

for col in df.select_dtypes(include="object").columns:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col].astype(str))
    encoders[col] = encoder

print("\nDataset Preview")
print(df.head())

# Features and target

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Train test split

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

# Train Naive Bayes

nb_model = GaussianNB()

nb_model.fit(X_train, y_train)

y_pred_nb = nb_model.predict(X_test)

print("\nNaive Bayes Classification Report")
print(classification_report(y_test, y_pred_nb))

# Train Random Forest

rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

print("\nRandom Forest Classification Report")
print(classification_report(y_test, y_pred_rf))

# First 22 predictions

comparison_predictions = pd.DataFrame({
    "Actual": y_test.values[:22],
    "Naive Bayes": y_pred_nb[:22],
    "Random Forest": y_pred_rf[:22]
})

print("\nFirst 22 Predictions")
print(comparison_predictions)

# Model comparison

comparison = pd.DataFrame({
    "Model": [
        "Naive Bayes",
        "Random Forest"
    ],
    "Accuracy": [
        accuracy_score(y_test, y_pred_nb),
        accuracy_score(y_test, y_pred_rf)
    ],
    "Precision": [
        precision_score(y_test, y_pred_nb, average="weighted"),
        precision_score(y_test, y_pred_rf, average="weighted")
    ],
    "Recall": [
        recall_score(y_test, y_pred_nb, average="weighted"),
        recall_score(y_test, y_pred_rf, average="weighted")
    ],
    "F1 Score": [
        f1_score(y_test, y_pred_nb, average="weighted"),
        f1_score(y_test, y_pred_rf, average="weighted")
    ]
})

print("\nModel Comparison")
print(comparison)

# Save comparison

comparison.to_csv(
    "comparison.csv",
    index=False
)

print("\ncomparison.csv Saved")

# Confusion matrix

cm = confusion_matrix(
    y_test,
    y_pred_rf,
    normalize="true"
)

plt.figure(figsize=(10,8))

sns.heatmap(
    cm,
    annot=True,
    fmt=".2f",
    cmap="Blues"
)

plt.title("Normalized Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.savefig(
    "confusion_matrix.png",
    bbox_inches="tight"
)

plt.show()

print("confusion_matrix.png Saved")

# Accuracy chart

plt.figure(figsize=(8,5))

plt.bar(
    comparison["Model"],
    comparison["Accuracy"]
)

plt.title("Naive Bayes vs Random Forest")
plt.ylabel("Accuracy")

plt.show()

# Select best model

nb_acc = accuracy_score(
    y_test,
    y_pred_nb
)

rf_acc = accuracy_score(
    y_test,
    y_pred_rf
)

if rf_acc > nb_acc:
    best_model = rf_model
    best_name = "Random Forest"
    best_score = rf_acc
else:
    best_model = nb_model
    best_name = "Naive Bayes"
    best_score = nb_acc

# Save best model

joblib.dump(
    best_model,
    "best_model.pkl"
)

print("\nbest_model.pkl Saved")

# Final output

print("\nFinal Selected Model")
print("Model :", best_name)
print("Accuracy :", round(best_score * 100, 2), "%")
