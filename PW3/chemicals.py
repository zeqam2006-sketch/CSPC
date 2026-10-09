import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("chemicals_cancer.csv")
print("Shape:", df.shape)
print(df.head())

# Task 6: naive association of each chemical with malignancy
print("\nNaive correlations with malignancy:")
for chem in ["benzene", "cadmium"]:
    r, p = stats.pearsonr(df[chem], df["malignancy"])
    print(chem, "r =", round(r, 3), " p =", p)

# Scatter plots
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, chem in zip(axes, ["benzene", "cadmium"]):
    ax.scatter(df[chem], df["malignancy"], alpha=0.5, s=12)
    ax.set_xlabel(chem)
    ax.set_ylabel("malignancy")
    ax.set_title("malignancy vs " + chem)
    ax.grid(True)
plt.tight_layout()
plt.savefig("naive_scatter.png", dpi=150)
plt.close()

# Task 7a: which variable could be a confounder?
print("\nCorrelation matrix:")
print(df.corr().round(2))

# Task 7b: restrict to similar pollution_index (45-55) and recompute
sub = df[(df["pollution_index"] > 45) & (df["pollution_index"] < 55)]
print("\nPatients with pollution_index in (45, 55):", len(sub))
r_b, p_b = stats.pearsonr(sub["benzene"], sub["malignancy"])
r_c, p_c = stats.pearsonr(sub["cadmium"], sub["malignancy"])
print("benzene r =", round(r_b, 3), " p =", p_b)
print("cadmium r =", round(r_c, 3), " p =", p_c)

# Task 7c: robustness check - repeat in five pollution bands
print("\nBands of pollution_index:")
for lo in range(0, 100, 20):
    band = df[(df["pollution_index"] >= lo) & (df["pollution_index"] < lo + 20)]
    rb, _ = stats.pearsonr(band["benzene"], band["malignancy"])
    rc, _ = stats.pearsonr(band["cadmium"], band["malignancy"])
    print(lo, "-", lo + 20, " n =", len(band),
          " benzene r =", round(rb, 2), " cadmium r =", round(rc, 2))

# Plot: naive vs controlled correlations
naive_b, _ = stats.pearsonr(df["benzene"], df["malignancy"])
naive_c, _ = stats.pearsonr(df["cadmium"], df["malignancy"])
x = [0, 1]
w = 0.35
plt.figure(figsize=(6, 5))
plt.bar([i - w / 2 for i in x], [naive_b, naive_c], w, label="all patients (naive)")
plt.bar([i + w / 2 for i in x], [r_b, r_c], w, label="pollution_index 45-55")
plt.xticks(x, ["benzene", "cadmium"])
plt.ylabel("Pearson r with malignancy")
plt.axhline(0, color="black")
plt.legend()
plt.grid(True)
plt.savefig("confounder_check.png", dpi=150)
plt.close()