import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV
)

from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Load Dataset

df = pd.read_csv("crop production.csv")

print("Dataset Shape")
print(df.shape)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

# Data Cleaning

df.dropna(inplace=True)

for col in df.select_dtypes(include="object").columns:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col].astype(str))

print("\nDataset Preview")
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

# Baseline Model

model = RandomForestClassifier(
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

baseline_accuracy = accuracy_score(
    y_test,
    y_pred
)

baseline_f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

print("\nBaseline Accuracy")
print(round(baseline_accuracy * 100, 2), "%")

print("\nBaseline F1 Score")
print(round(baseline_f1, 4))

# Cross Validation

cv_scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="f1_weighted"
)

print("\nCross Validation Scores")
print(cv_scores)

print("\nMean CV Score")
print(round(cv_scores.mean(), 4))

print("\nStandard Deviation")
print(round(cv_scores.std(), 4))

# Chart 1

plt.figure(figsize=(8,5))

plt.plot(
    range(1, 6),
    cv_scores,
    marker="o"
)

plt.title("Cross Validation Scores")
plt.xlabel("Fold")
plt.ylabel("F1 Score")

plt.savefig("cross_validation_scores.png")

plt.show()

# Parameter Grid

param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [10, 20, 30],
    "min_samples_split": [2, 5, 10]
}

# Improved Model

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring="f1_weighted",
    n_jobs=-1
)

grid.fit(X_train, y_train)

print("\nBest Parameters")
print(grid.best_params_)

print("\nBest Cross Validation Score")
print(round(grid.best_score_, 4))

# Tuned Model

tuned_model = grid.best_estimator_

y_pred_tuned = tuned_model.predict(X_test)

tuned_accuracy = accuracy_score(
    y_test,
    y_pred_tuned
)

tuned_f1 = f1_score(
    y_test,
    y_pred_tuned,
    average="weighted"
)

print("\nTuned Accuracy")
print(round(tuned_accuracy * 100, 2), "%")

print("\nTuned F1 Score")
print(round(tuned_f1, 4))

# Comparison Table

comparison = pd.DataFrame({
    "Model": [
        "Day 6 Model",
        "Day 8 Tuned Model"
    ],
    "Accuracy": [
        baseline_accuracy,
        tuned_accuracy
    ],
    "F1 Score": [
        baseline_f1,
        tuned_f1
    ]
})

print("\nBefore vs After Comparison")
print(comparison)

comparison.to_csv(
    "comparison.csv",
    index=False
)

# Chart 2

plt.figure(figsize=(8,5))

plt.bar(
    comparison["Model"],
    comparison["Accuracy"]
)

plt.title("Day 6 vs Day 8 Accuracy")
plt.ylabel("Accuracy")

plt.savefig("before_after_comparison.png")

plt.show()

# Validation Curve

results = pd.DataFrame(
    grid.cv_results_
)

validation_data = results.groupby(
    "param_n_estimators"
)["mean_test_score"].mean()

# Chart 3

plt.figure(figsize=(8,5))

plt.plot(
    validation_data.index,
    validation_data.values,
    marker="o"
)

plt.title("Validation Curve")
plt.xlabel("n_estimators")
plt.ylabel("Mean CV Score")

plt.savefig("validation_curve.png")

plt.show()

# Confusion Matrix

cm = confusion_matrix(
    y_test,
    y_pred_tuned,
    normalize="true"
)

# Chart 4

plt.figure(figsize=(10,8))

sns.heatmap(
    cm,
    annot=True,
    fmt=".2f",
    cmap="Blues"
)

plt.title("Tuned Model Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.savefig("confusion_matrix.png")

plt.show()

# Classification Report

print("\nClassification Report")

print(
    classification_report(
        y_test,
        y_pred_tuned
    )
)

# Save Tuned Model

joblib.dump(
    tuned_model,
    "tuned_model.pkl"
)

# Final Output

print("\nFinal Selected Model")
print("Random Forest (Tuned)")

print("\nDay 6 Accuracy")
print(round(baseline_accuracy * 100, 2), "%")

print("\nDay 8 Accuracy")
print(round(tuned_accuracy * 100, 2), "%")

print("\nAccuracy Improvement")
print(
    round(
        (tuned_accuracy - baseline_accuracy) * 100,
        2
    ),
    "%"
)

print("\nBaseline F1 Score")
print(round(baseline_f1, 4))

print("\nTuned F1 Score")
print(round(tuned_f1, 4))

print("\nBest Parameters")
print(grid.best_params_)

print("\nGenerated Files")
print("cross_validation_scores.png")
print("before_after_comparison.png")
print("validation_curve.png")
print("confusion_matrix.png")
print("comparison.csv")
print("tuned_model.pkl")
