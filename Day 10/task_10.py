import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import validation_curve

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("crop production.csv")

print(df.head())

# ==========================================
# FEATURES AND TARGET
# ==========================================

X = df.drop("label", axis=1)
y = df["label"]

# ==========================================
# ENCODE TARGET
# ==========================================

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# ==========================================
# FEATURE SCALING
# ==========================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# NAIVE BAYES MODEL
# ==========================================

from sklearn.naive_bayes import GaussianNB

nb_model = GaussianNB()

nb_model.fit(X_train_scaled, y_train)

nb_pred = nb_model.predict(X_test_scaled)

nb_accuracy = accuracy_score(y_test, nb_pred)

print("Naive Bayes Accuracy :", round(nb_accuracy * 100, 2), "%")


# ==========================================
# RANDOM FOREST MODEL
# ==========================================

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train_scaled, y_train)

rf_pred = rf_model.predict(X_test_scaled)

rf_accuracy = accuracy_score(y_test, rf_pred)

print("Random Forest Accuracy :", round(rf_accuracy * 100, 2), "%")


# ==========================================
# MODEL COMPARISON
# ==========================================

print("\nMODEL COMPARISON")
print("----------------------------")
print("Naive Bayes   :", round(nb_accuracy * 100, 2), "%")
print("Random Forest :", round(rf_accuracy * 100, 2), "%")

if rf_accuracy > nb_accuracy:
    print("Best Model : Random Forest")
else:
    print("Best Model : Naive Bayes")

# ==========================================
# TRAIN MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train_scaled, y_train)

# ==========================================
# MODEL ACCURACY
# ==========================================

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# ==========================================
# CREATE CHARTS
# ==========================================

import os
os.makedirs("charts", exist_ok=True)

# 1. Feature Importance Chart

importances = model.feature_importances_

plt.figure(figsize=(8,5))
plt.bar(X.columns, importances)
plt.xticks(rotation=45)
plt.title("Feature Importance")
plt.tight_layout()
plt.savefig("charts/feature_importance.png")
plt.close()

# 2. Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix")
plt.savefig("charts/confusion_matrix.png")
plt.close()

# 3. Validation Curve

param_range = [10, 50, 100, 150, 200]

train_scores, test_scores = validation_curve(
    RandomForestClassifier(random_state=42),
    X_train_scaled,
    y_train,
    param_name="n_estimators",
    param_range=param_range,
    cv=3,
    scoring="accuracy"
)

train_mean = train_scores.mean(axis=1)
test_mean = test_scores.mean(axis=1)

plt.figure(figsize=(8,5))
plt.plot(param_range, train_mean, marker="o", label="Training")
plt.plot(param_range, test_mean, marker="o", label="Validation")
plt.xlabel("n_estimators")
plt.ylabel("Accuracy")
plt.title("Validation Curve")
plt.legend()
plt.savefig("charts/validation_curve.png")
plt.close()

print("Charts saved successfully!")

# ==========================================
# SAVE FILES
# ==========================================

joblib.dump(model, "final_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("All files saved successfully!")

# ==========================================
# LOAD FILES CHECK
# ==========================================

model = joblib.load("final_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

import os

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/final_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(label_encoder, "models/label_encoder.pkl")

print("All files loaded successfully!")

print("\n========== HANDOFF CHECKLIST ==========")

print("Required Files:")
print("1. final_model.pkl")
print("2. scaler.pkl")
print("3. label_encoder.pkl")

print("\nInput Columns Order:")
print("N, P, K, temperature, humidity, ph, rainfall")

print("\nOutput Format:")
print("{'prediction':'Crop Name','confidence':'95.2%'}")

# ==========================================
# PREDICT FUNCTION
# ==========================================

def predict(inputs):

    try:

        model = joblib.load("final_model.pkl")
        scaler = joblib.load("scaler.pkl")
        encoder = joblib.load("label_encoder.pkl")
        input_df = pd.DataFrame([inputs])
        for value in inputs.values():
            if value<0:
                raise ValueError("Negative values are not allowed")
        scaled_input = scaler.transform(input_df)

        prediction = model.predict(scaled_input)[0]

        confidence = max(
            model.predict_proba(scaled_input)[0]
        )

        crop = encoder.inverse_transform(
            [prediction]
        )[0]

        return {
            "prediction": crop,
            "confidence": f"{confidence*100:.2f}%"
        }

    except Exception as e:

        return {
            "prediction": "Error",
            "confidence": "N/A",
            "error": str(e)
        }

# ==========================================
# SAMPLE TEST
# ==========================================

sample = {
    "N": 90,
    "P": 42,
    "K": 43,
    "temperature": 20.8,
    "humidity": 82,
    "ph": 6.5,
    "rainfall": 202
}

print("\nPrediction Result:")
print(predict(sample))
# ==========================================
# TEST CASES
# ==========================================

test_cases = [

    {"N": 90, "P": 42, "K": 43,
     "temperature": 20.8, "humidity": 82,
     "ph": 6.5, "rainfall": 202},

    {"N": 85, "P": 58, "K": 41,
     "temperature": 22.0, "humidity": 80,
     "ph": 6.4, "rainfall": 180},

    {"N": 60, "P": 35, "K": 35,
     "temperature": 25, "humidity": 70,
     "ph": 6.8, "rainfall": 150},

    {"N": 120, "P": 80, "K": 80,
     "temperature": 35, "humidity": 90,
     "ph": 7.5, "rainfall": 300},

    {"N": 130, "P": 90, "K": 90,
     "temperature": 38, "humidity": 95,
     "ph": 8.0, "rainfall": 350},

    {"N": 0, "P": 0, "K": 0,
     "temperature": 0, "humidity": 0,
     "ph": 0, "rainfall": 0},

    {"N": 140, "P": 145, "K": 205,
     "temperature": 45, "humidity": 100,
     "ph": 14, "rainfall": 400},

    {"N": 70, "P": 40, "K": 40,
     "temperature": 23, "humidity": 75,
     "ph": 6.5, "rainfall": 180},

    {"N": 100, "P": 60, "K": 50,
     "temperature": 28, "humidity": 85,
     "ph": 6.8, "rainfall": 220},

    {"N": -10, "P": -20, "K": -30,
     "temperature": -5, "humidity": -10,
     "ph": -1, "rainfall": -50}
]

results = []

for i, case in enumerate(test_cases, start=1):

    result = predict(case)

    results.append({
        "Case": i,
        "Prediction": result.get("prediction"),
        "Confidence": result.get("confidence"),
        "Status": "PASS"
        if result.get("prediction") != "Error"
        else "ERROR"
    })

results_df = pd.DataFrame(results)

print("\n========== TEST RESULTS ==========")
print(results_df.to_string(index=False))

# ==========================================
# MODEL SUMMARY CARD
# ==========================================

print("\n")
print("==========================================")
print("MODEL SUMMARY CARD")
print("==========================================")

print("Project : Smart Crop Recommendation Engine")
print("Domain : Agriculture")

print("\nAlgorithm")
print("Random Forest Classifier")

print("\nDataset")
print("Crop Recommendation Dataset")
print("Rows : 2200")
print("Features : 7")

print("\nFinal Performance")
print("Accuracy :", round(accuracy * 100, 2), "%")

print("\nInput Features")
print("1. N")
print("2. P")
print("3. K")
print("4. temperature")
print("5. humidity")
print("6. ph")
print("7. rainfall")

print("\nRequired PKL Files")
print("final_model.pkl -> Trained Random Forest")
print("scaler.pkl -> StandardScaler")
print("label_encoder.pkl -> Crop Label Encoder")

print("\nSample Input")
print(sample)

print("\nSample Output")
print(predict(sample))



print("==========================================")
