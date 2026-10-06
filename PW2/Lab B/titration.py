"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.

# TODO 1: read the data
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]
pH = data[:, 1]


# TODO 2: slope of the pH curve and the equivalence point
slope = np.gradient(pH, V)
i_eq = np.argmax(slope)
V_eq = V[i_eq]
print("Equivalence point at V =", V_eq, "mL")
print("pH at the equivalence point:", pH[i_eq])
print("Largest slope:", slope[i_eq], "pH units per mL")


# TODO 3: two plots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

ax1.plot(V, pH, color="blue")
ax1.axvline(V_eq, color="red", linestyle="--", label=f"Equivalence point ({V_eq:.1f} mL)")
ax1.set_xlabel("Volume of base (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration curve")
ax1.legend()

ax2.plot(V, slope, color="green")
ax2.axvline(V_eq, color="red", linestyle="--", label=f"Peak at {V_eq:.1f} mL")
ax2.set_xlabel("Volume of base (mL)")
ax2.set_ylabel("Slope (pH per mL)")
ax2.set_title("Slope of the titration curve")
ax2.legend()

plt.tight_layout()
plt.savefig("titration.png", dpi=150)
