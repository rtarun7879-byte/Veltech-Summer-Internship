import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset

data = pd.read_csv(r"D:\veltech summerintenship\day 4\crop production.csv")

# Display first 5 rows

print(data.head())

# ==========================
# Feature Comparison 1
# Temperature vs Rainfall
# ==========================

plt.figure(figsize=(8,5))

plt.scatter(
    data["temperature"],
    data["rainfall"]
)

plt.title("Temperature vs Rainfall")

plt.xlabel("Temperature")

plt.ylabel("Rainfall")

plt.grid(True)

plt.savefig("Temperature_vs_Rainfall.png")

plt.show()

# ==========================
# Feature Comparison 2
# Humidity vs Rainfall
# ==========================

plt.figure(figsize=(8,5))

plt.scatter(
    data["humidity"],
    data["rainfall"]
)

plt.title("Humidity vs Rainfall")

plt.xlabel("Humidity")

plt.ylabel("Rainfall")

plt.grid(True)

plt.savefig("Humidity_vs_Rainfall.png")

plt.show()

print("Task 5 Completed Successfully")
