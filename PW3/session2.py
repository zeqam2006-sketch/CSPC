import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")

# Task 4a: split thalach into two groups by target
disease = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]
print("n disease =", len(disease), " n healthy =", len(healthy))

# Normality of each group (Shapiro-Wilk, H0: normal)
for name, g in [("disease", disease), ("healthy", healthy)]:
    W, p = stats.shapiro(g)
    print("Shapiro", name, "W =", round(W, 4), "p =", p)

# thalach is not normal (Session 1) -> Mann-Whitney U, two-tailed
u, p = stats.mannwhitneyu(disease, healthy, alternative="two-sided")
print("\nMann-Whitney U =", u, " p =", p)
if p < 0.05:
    print("reject H0: the two groups differ")
else:
    print("fail to reject H0: cannot claim a difference")

# Task 4b: mean and standard error for each group
means, ses = [], []
for name, g in [("disease", disease), ("healthy", healthy)]:
    m = g.mean()
    se = g.std(ddof=1) / np.sqrt(len(g))
    means.append(m)
    ses.append(se)
    print(name, "mean =", round(m, 2), " SE =", round(se, 2),
          " 95% CI = [", round(m - 2 * se, 2), ",", round(m + 2 * se, 2), "]")

# Plot: the two means with error bars (+- 1 SE)
plt.figure(figsize=(5, 5))
plt.errorbar(["disease", "healthy"], means, yerr=ses, fmt="o",
             capsize=8, markersize=8, color="black")
plt.ylabel("thalach (mean +- SE)")
plt.title("Mean max heart rate by group")
plt.grid(True)
plt.savefig("thalach_means.png", dpi=150)
plt.close()

# Task 5: correlation between age and thalach
r, p_r = stats.pearsonr(df["age"], df["thalach"])
rho, p_s = stats.spearmanr(df["age"], df["thalach"])
print("\nPearson  r   =", round(r, 3), " p =", p_r)
print("Spearman rho =", round(rho, 3), " p =", p_s)

# Scatter plot with a trend line
slope, intercept = np.polyfit(df["age"], df["thalach"], 1)
x = np.linspace(df["age"].min(), df["age"].max(), 100)

plt.figure(figsize=(7, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.6, color="steelblue")
plt.plot(x, slope * x + intercept, color="red")
plt.xlabel("age")
plt.ylabel("thalach (max heart rate)")
plt.title("age vs thalach, r = " + str(round(r, 2)))
plt.grid(True)
plt.savefig("age_thalach.png", dpi=150)
plt.close()

# Bonus: entropy of categorical columns
print("\nEntropy (bits):")
for col in ["target", "sex"]:
    p = df[col].value_counts(normalize=True)
    H = -(p * np.log2(p)).sum()
    print(col, "proportions:", p.round(3).to_dict(), " H =", round(H, 4), "bits")