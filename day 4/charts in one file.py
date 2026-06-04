import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# MANUAL DATASET
# ==========================

data = {
    "N":[90,85,60,74,78,69,69,94,89,68,91,90,78,93,94,60,85,91,77,88],
    "P":[42,58,55,35,42,37,55,53,54,58,53,46,58,56,50,48,38,35,38,35],
    "K":[43,41,44,40,42,42,38,40,38,38,40,42,44,36,37,39,41,39,36,40],
    "temperature":[20.87,21.77,23.00,26.49,20.13,23.05,22.70,20.27,24.51,23.22,
                   26.52,23.97,26.80,24.01,25.66,24.28,21.58,23.79,21.86,23.57],
    "humidity":[82.00,80.31,82.32,80.15,81.60,83.37,82.63,82.89,83.53,83.03,
                81.41,81.45,80.88,82.05,80.66,80.30,82.78,80.41,80.19,83.58],
    "rainfall":[202.93,226.65,263.96,242.86,262.71,251.05,271.32,241.97,230.44,
                221.20,264.61,250.08,284.43,185.27,209.58,231.08,276.65,206.26,
                224.55,291.29],
    "label":[
        "rice","rice","rice","rice","rice",
        "maize","maize","maize","maize","maize",
        "chickpea","chickpea","chickpea","chickpea","chickpea",
        "rice","rice","maize","chickpea","rice"
    ]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully")
print(df.head())

# ==========================
# GRAPH 1 : BAR CHART
# ==========================

plt.figure(figsize=(8,5))

crop_count = df["label"].value_counts()

plt.bar(crop_count.index, crop_count.values)

plt.title("Crop Count")

plt.xlabel("Crop Type")

plt.ylabel("Count")

plt.savefig("Graph1_BarChart.png")

plt.close()

# ==========================
# GRAPH 2 : SCATTER PLOT
# ==========================

plt.figure(figsize=(8,5))

plt.scatter(df["temperature"], df["humidity"])

plt.title("Temperature vs Humidity")

plt.xlabel("Temperature")

plt.ylabel("Humidity")

plt.savefig("Graph2_ScatterPlot.png")

plt.close()

# ==========================
# GRAPH 3 : HISTOGRAM
# ==========================

plt.figure(figsize=(8,5))

plt.hist(df["rainfall"], bins=8)

plt.title("Rainfall Distribution")

plt.xlabel("Rainfall")

plt.ylabel("Frequency")

plt.savefig("Graph3_Histogram.png")

plt.close()

# ==========================
# GRAPH 4 : LINE CHART
# ==========================

avg_values = df[["N","P","K"]].mean()

plt.figure(figsize=(8,5))

plt.plot(avg_values.index,
         avg_values.values,
         marker="o")

plt.title("Average N P K Values")

plt.xlabel("Nutrient")

plt.ylabel("Average Value")

plt.grid(True)

plt.savefig("Graph4_LineChart.png")

plt.close()

print("All 4 graphs created successfully.")
print("Saved files:")
print("Graph1_BarChart.png")
print("Graph2_ScatterPlot.png")
print("Graph3_Histogram.png")
print("Graph4_LineChart.png")
