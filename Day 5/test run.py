import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# ==================================================
# 1. READ DATASET
# ==================================================

df = pd.read_csv("crop production.csv")

# ==================================================
# 2. DATA EXPLORATION FUNCTIONS
# ==================================================

print(df.head())                 # 1
print(df.tail())                 # 2
print(df.info())                 # 3
print(df.describe())             # 4
print(df.shape)                  # 5
print(df.columns)                # 6
print(df.index)                  # 7
print(df.dtypes)                 # 8
print(df.memory_usage())         # 9

# ==================================================
# 3. SELECTION FUNCTIONS
# ==================================================

print(df.loc[0:5])               # 10
print(df.iloc[0:5])              # 11

print(df.sample(5))              # 12

print(df.nlargest(5,'rainfall')) # 13
print(df.nsmallest(5,'rainfall'))# 14

# ==================================================
# 4. CLEANING FUNCTIONS
# ==================================================

print(df.isnull().sum())         # 15

print(df.duplicated().sum())     # 16

df = df.drop_duplicates()        # 17

df = df.fillna(0)                # 18

# ==================================================
# 5. SORTING FUNCTIONS
# ==================================================

print(df.sort_values('temperature')) #19

print(df.sort_index())               #20

# ==================================================
# 6. AGGREGATION FUNCTIONS
# ==================================================

print(df.groupby('label').mean(numeric_only=True)) #21

print(df['rainfall'].mean())     #22

print(df['rainfall'].max())      #23

print(df['rainfall'].min())      #24

print(df['rainfall'].std())      #25

print(df['rainfall'].sum())      #26

# ==================================================
# 7. CATEGORICAL FUNCTIONS
# ==================================================

print(df['label'].value_counts()) #27

print(df['label'].unique())       #28

print(df['label'].nunique())      #29

# ==================================================
# 8. INDEX FUNCTIONS
# ==================================================

temp = df.set_index('label')      #30

temp = temp.reset_index()         #31

# ==================================================
# 9. FILE OUTPUT
# ==================================================

df.to_csv("processed_crop_data.csv", index=False)

# ==================================================
# 10. GRAPH 1
# ==================================================

crop_counts = df['label'].value_counts()

plt.figure(figsize=(10,5))
crop_counts.plot(kind='bar')
plt.title("Crop Distribution")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("crop_distribution.png")
plt.close()

# ==================================================
# 11. GRAPH 2
# ==================================================

plt.figure(figsize=(8,5))
plt.hist(df['rainfall'], bins=20)
plt.title("Rainfall Distribution")
plt.tight_layout()
plt.savefig("rainfall_distribution.png")
plt.close()

# ==================================================
# 12. GRAPH 3
# ==================================================

plt.figure(figsize=(8,5))
plt.scatter(df['temperature'], df['humidity'])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Temperature vs Humidity")
plt.tight_layout()
plt.savefig("temp_vs_humidity.png")
plt.close()

# ==================================================
# 13. MACHINE LEARNING
# ==================================================

X = df.drop('label', axis=1)

y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# ==================================================
# 14. SAVE PKL FILE
# ==================================================

with open("crop_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully")

# ==================================================
# 15. TEST PREDICTION
# ==================================================

sample = [[90,42,43,20.8,82,6.5,202]]

prediction = model.predict(sample)

print("Recommended Crop:", prediction[0])


# ==========================================
# ACCURACY CHECK AND PNG GENERATION
# ==========================================

import matplotlib.pyplot as plt

accuracy_percent = accuracy * 100

if accuracy_percent > 70:
    print(f"Accuracy is greater than 70% : {accuracy_percent:.2f}%")
else:
    print(f"Accuracy is less than or equal to 70% : {accuracy_percent:.2f}%")

plt.figure(figsize=(10,5))

plt.text(
    0.5,
    0.5,
    f"Accuracy : {accuracy_percent:.2f}%",
    fontsize=28,
    ha="center",
    va="center",
    color="green"
)

plt.axis("off")

plt.savefig(
    "accuracy_result.png",
    bbox_inches="tight"
)

plt.close()

print("accuracy_result.png generated successfully")
