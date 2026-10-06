"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.

# TODO 1: read the data
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = C[0]


# TODO 2: total error for a given k
def total_error(k):
    model = C0 * np.exp(-k * t)
    return np.sum((C - model) ** 2)


# TODO 3: minimise the error
res = minimize(total_error, x0=0.5, method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print("Fitted k:", k_fit)


# TODO 4: plot the data and the fitted curve
t_fine = np.linspace(t.min(), t.max(), 200)
plt.figure(figsize=(7, 5))
plt.scatter(t, C, color="blue", label="Measured data")
plt.plot(t_fine, C0 * np.exp(-k_fit * t_fine), color="red",
         label=f"Fitted curve (k = {k_fit:.3f})")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("First-order reaction: fit of the rate constant")
plt.legend()
plt.tight_layout()
plt.savefig("kinetics.png", dpi=150)
