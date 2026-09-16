import numpy as np
import matplotlib.pyplot as plt

# Given decay constant
LAMBDA = 0.3

# TODO 1: Read the data skipping the header row
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# TODO 2: Set N0 to the first observed value and compute analytical law
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: Create a 1x2 subplot with shared x and y axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 5))

# Left plot: Observed data (scatter points)
ax1.scatter(t, observed, color="blue", label="Observed Data", alpha=0.7)
ax1.set_title("Observed Decay")
ax1.set_xlabel("Time (t)")
ax1.set_ylabel("Count (N)")
ax1.legend()
ax1.grid(True)

# Right plot: Analytical law (smooth line)
ax2.plot(t, analytical, color="red", label="Analytical Law", linewidth=2)
ax2.set_title("Analytical Decay ($N_0 e^{-\\lambda t}$)")
ax2.set_xlabel("Time (t)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()

# TODO 4: Save the figure as figure.png
plt.savefig("figure.png")
print("figure.png successfully generated.")