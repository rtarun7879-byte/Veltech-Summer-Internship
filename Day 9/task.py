import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("crop production.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# =====================================================
# FEATURES AND TARGET
# =====================================================

X = df.drop("label", axis=1)
y = df["label"]

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================================
# TRAIN MODEL
# =====================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# =====================================================
# MODEL ACCURACY
# =====================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

# =====================================================
# TASK 1
# FEATURE IMPORTANCE
# =====================================================

importances = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importances
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=True
)

plt.figure(figsize=(8,5))

plt.barh(
    importance_df["Feature"],
    importance_df["Importance"]
)

plt.title("Feature Importance")
plt.xlabel("Importance Score")

plt.tight_layout()

plt.savefig("Day9_Fix1_FeatureImportance.png")

plt.close()

print("Day9_Fix1_FeatureImportance.png Saved")

# =====================================================
# TASK 2
# CLASS DISTRIBUTION
# =====================================================

class_counts = y.value_counts()

plt.figure(figsize=(10,5))

class_counts.plot(kind="bar")

plt.title("Crop Class Distribution")
plt.xlabel("Crop")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("Day9_Fix2_ClassImbalance.png")

plt.close()

print("Day9_Fix2_ClassImbalance.png Saved")

# =====================================================
# TASK 3
# EXPLAINABILITY
# =====================================================

top3 = importance_df.sort_values(
    by="Importance",
    ascending=False
).head(3)

plt.figure(figsize=(6,4))

plt.bar(
    top3["Feature"],
    top3["Importance"]
)

plt.title("Top 3 Important Features")

plt.ylabel("Importance")

plt.tight_layout()

plt.savefig("Day9_Fix3_Explainability.png")

plt.close()

print("Day9_Fix3_Explainability.png Saved")

# =====================================================
# TASK 4
# OUTPUT ENRICHMENT
# =====================================================

sample_input = X.iloc[[0]]

probabilities = model.predict_proba(sample_input)[0]

crop_labels = model.classes_

top_3_indices = probabilities.argsort()[-3:][::-1]

crops = []
confidence = []

print("\nTop 3 Recommended Crops")

for idx in top_3_indices:

    crops.append(crop_labels[idx])

    confidence.append(probabilities[idx] * 100)

    print(
        crop_labels[idx],
        "-",
        round(probabilities[idx] * 100, 2),
        "%"
    )

plt.figure(figsize=(8,5))

plt.bar(
    crops,
    confidence
)

plt.title("Top 3 Recommended Crops")
plt.ylabel("Confidence (%)")

for i, v in enumerate(confidence):

    plt.text(
        i,
        v + 1,
        f"{v:.1f}%"
    )

plt.tight_layout()

plt.savefig("Day9_Fix4_OutputEnrichment.png")

plt.close()

print("Day9_Fix4_OutputEnrichment.png Saved")

# =====================================================
# TASK 5
# END TO END TEST
# =====================================================

samples = [

    {
        'N':90,
        'P':42,
        'K':43,
        'temperature':20.8,
        'humidity':82,
        'ph':6.5,
        'rainfall':202
    },

    {
        'N':120,
        'P':48,
        'K':50,
        'temperature':25.5,
        'humidity':75,
        'ph':6.8,
        'rainfall':180
    },

    {
        'N':60,
        'P':35,
        'K':30,
        'temperature':29.2,
        'humidity':65,
        'ph':7.0,
        'rainfall':120
    },

    {
        'N':100,
        'P':55,
        'K':40,
        'temperature':22.0,
        'humidity':85,
        'ph':6.2,
        'rainfall':250
    },

    {
        'N':75,
        'P':40,
        'K':35,
        'temperature':27.0,
        'humidity':70,
        'ph':6.7,
        'rainfall':150
    }

]

results = []

for sample in samples:

    sample_df = pd.DataFrame([sample])

    prediction = model.predict(sample_df)[0]

    probability = max(
        model.predict_proba(sample_df)[0]
    ) * 100

    results.append(
        [
            prediction,
            round(probability, 2)
        ]
    )

result_df = pd.DataFrame(
    results,
    columns=[
        "Predicted Crop",
        "Confidence (%)"
    ]
)

print("\nEnd To End Results")
print(result_df)

fig, ax = plt.subplots(figsize=(8,3))

ax.axis('off')

table = ax.table(
    cellText=result_df.values,
    colLabels=result_df.columns,
    loc='center'
)

table.auto_set_font_size(False)

table.set_fontsize(10)

table.scale(1.2, 1.5)

plt.tight_layout()

plt.savefig("Day9_Fix5_EndToEndTest.png")

plt.close()

print("Day9_Fix5_EndToEndTest.png Saved")

print("\nALL DAY 9 TASKS COMPLETED SUCCESSFULLY")
