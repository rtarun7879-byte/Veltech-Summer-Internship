import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# MANUAL DATASET
# ==========================

data = {
    "N":[90,85,60,74,78,69,69,94,89,68,91,90,78,93,94,60,85,91,77,88],
    "P":[42,58,55,35,42,37,55,53,54,58,53,46,58,56,50,48,38,35,38,35],
    "K":[43,41,44,40,42,42,38,40,38,38,40,42,44,36,37,39,41,39,36,40]
}

df = pd.DataFrame(data)

# ==========================
# CALCULATE AVERAGES
# ==========================

average_n = df["N"].mean()

average_p = df["P"].mean()

average_k = df["K"].mean()

# Store averages

nutrients = ["Nitrogen (N)", "Phosphorus (P)", "Potassium (K)"]

average_values = [average_n, average_p, average_k]

# ==========================
# CALCULATE OVERALL MEAN
# ==========================

overall_mean = sum(average_values) / len(average_values)

# ==========================
# CUSTOM BAR CHART
# ==========================

plt.figure(figsize=(10,6))

colors = ["red", "green", "blue"]

plt.bar(
    nutrients,
    average_values,
    color=colors,
    label="Average Nutrient Value"
)

# Mean Line

plt.axhline(
    y=overall_mean,
    color="black",
    linestyle="--",
    linewidth=2,
    label="Overall Mean"
)

# ==========================
# CHART CUSTOMIZATION
# ==========================

plt.title("Average Nutrient Values in Crop Dataset")

plt.xlabel("Nutrients")

plt.ylabel("Average Value")

plt.legend()

plt.grid(axis="y")

# Save graph

plt.savefig("Task2_Custom_Styled_Chart.png")

# Show graph

plt.show()

# ==========================
# OUTPUT
# ==========================

print("Average N :", average_n)

print("Average P :", average_p)

print("Average K :", average_k)

print("Overall Mean :", overall_mean)

print("Task 2 Completed Successfully")

import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# MANUAL DATASET
# ==========================

data = {
    "N":[90,85,60,74,78,69,69,94,89,68,91,90,78,93,94,60,85,91,77,88],
    "P":[42,58,55,35,42,37,55,53,54,58,53,46,58,56,50,48,38,35,38,35],
    "K":[43,41,44,40,42,42,38,40,38,38,40,42,44,36,37,39,41,39,36,40]
}

df = pd.DataFrame(data)

# ==========================
# CALCULATE AVERAGES
# ==========================

average_n = df["N"].mean()

average_p = df["P"].mean()

average_k = df["K"].mean()

# Store averages

nutrients = ["Nitrogen (N)", "Phosphorus (P)", "Potassium (K)"]

average_values = [average_n, average_p, average_k]

# ==========================
# CALCULATE OVERALL MEAN
# ==========================

overall_mean = sum(average_values) / len(average_values)

# ==========================
# CUSTOM BAR CHART
# ==========================

plt.figure(figsize=(10,6))

colors = ["red", "green", "blue"]

plt.bar(
    nutrients,
    average_values,
    color=colors,
    label="Average Nutrient Value"
)

# Mean Line

plt.axhline(
    y=overall_mean,
    color="black",
    linestyle="--",
    linewidth=2,
    label="Overall Mean"
)

# ==========================
# CHART CUSTOMIZATION
# ==========================

plt.title("Average Nutrient Values in Crop Dataset")

plt.xlabel("Nutrients")

plt.ylabel("Average Value")

plt.legend()

plt.grid(axis="y")

# Save graph

plt.savefig("Task2_Custom_Styled_Chart.png")

# Show graph

plt.show()

# ==========================
# OUTPUT
# ==========================

print("Average N :", average_n)

print("Average P :", average_p)

print("Average K :", average_k)

print("Overall Mean :", overall_mean)

print("Task 2 Completed Successfully")
