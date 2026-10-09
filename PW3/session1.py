import pandas as pd

# Load the heart disease dataset
df = pd.read_csv("heart.csv")

# Shape and first rows
print("Shape (rows, columns):", df.shape)
print(df.head())

# Isolate the four continuous columns
cont = df[["age", "chol", "trestbps", "thalach"]]
print(cont.head())
print(cont.describe())

import matplotlib.pyplot as plt

# Task 2: histograms of the four continuous variables
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
colors = ["steelblue", "indianred", "seagreen", "darkorange"]

for ax, col, color in zip(axes.flatten(), cont.columns, colors):
    ax.hist(cont[col], bins=20, color=color, edgecolor="black")
    ax.set_title(col)
    ax.set_xlabel(col)
    ax.set_ylabel("count")
    ax.grid(True)  # notebook-style grid

plt.tight_layout()
plt.savefig("histograms.png", dpi=150)
plt.close()

from scipy import stats

# Task 3a: Q-Q plots against the normal distribution
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flatten(), cont.columns):
    stats.probplot(cont[col], dist="norm", plot=ax)
    ax.set_title("Q-Q plot: " + col)
    ax.grid(True)
plt.tight_layout()
plt.savefig("qqplots.png", dpi=150)
plt.close()

# Task 3b: Shapiro-Wilk test (H0: the data is normal)
print("\nShapiro-Wilk test:")
for col in cont.columns:
    W, p = stats.shapiro(cont[col])
    if p < 0.05:
        verdict = "NOT normal (reject H0)"
    else:
        verdict = "normal OK (fail to reject H0)"
    print(col, "W =", round(W, 4), "p =", p, "->", verdict)