"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.

# TODO 1: the imbalance function (zero at equilibrium)
def k_imbalance(x):
    return (2 * x) ** 2 / ((a - x) * (b - x)) - K


# TODO 2 (method 1): root-finding with Newton
x_newton = newton(k_imbalance, x0=0.5)
print("Newton (root-finding): x =", x_newton)


# TODO 3 (method 2): minimisation with SLSQP
res = minimize(lambda x: k_imbalance(x[0]) ** 2, x0=[0.5],
               method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]
print("SLSQP (minimisation): x =", x_slsqp)
print("Difference between the two answers:", abs(x_newton - x_slsqp))


# TODO 4: equilibrium amounts and the plot
x_eq = x_newton
n_H2 = a - x_eq
n_I2 = b - x_eq
n_HI = 2 * x_eq
print(f"Equilibrium: H2 = {n_H2:.4f} mol, I2 = {n_I2:.4f} mol, HI = {n_HI:.4f} mol")

x_grid = np.linspace(0, 1, 200)
plt.figure(figsize=(7, 5))
plt.plot(x_grid, a - x_grid, color="blue", label="H2")
plt.plot(x_grid, b - x_grid, color="green", linestyle="--", label="I2")
plt.plot(x_grid, 2 * x_grid, color="red", label="HI")
plt.axvline(x_eq, color="black", linestyle=":", label=f"Equilibrium (x = {x_eq:.3f})")
plt.scatter([x_eq] * 3, [n_H2, n_I2, n_HI], color="black", zorder=5)
plt.xlabel("Extent of reaction x (mol)")
plt.ylabel("Amount (mol)")
plt.title("H2 + I2 <=> 2 HI: amounts vs extent")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("equilibrium.png", dpi=150)
