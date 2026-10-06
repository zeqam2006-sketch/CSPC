# CSPC Computer Science for Physics and Chemistry

My coursework repository. Each practical is under `PW<n>/Lab <X>/`.

## Setup

Create the environment for a given lab with `conda env create -f "PW<n>/Lab <X>/environment.yml"`, then run `conda activate cspc`.

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- The CSPC repository with a conda environment (`environment.yml`), the decay simulation files, three pytest tests and a speed comparison script, all pushed to GitHub.

**Speed comparison (loop vs NumPy):**
- loop : 3.5814 s
- numpy : 0.0003 s
- speed-up: 13502.6 x faster

**Tests:** all passing? yes (3 passed)

**Conclusion:**
- The repository, the environment and the tests all worked. The NumPy version is thousands of times faster than the pure Python loop because it decides all atoms at once with one binomial draw instead of looping over every atom. The exact speed-up changes a little from run to run, because the NumPy time is very small.

## PW1 - Lab B

![Decay Analysis](PW1/Lab%20B/figure.png)

### Data Analysis & Results
The observed data (`decay_observed.csv`) represents a decay process over time. Upon plotting the side-by-side comparison, the scatter points of the observed dataset match the analytical decay law ($N(t) = N_0 e^{-\lambda t}$) with $\lambda = 0.3$.

### Automation
The Snakemake pipeline automates the generation of `figure.png` from `decay_observed.csv` via `plot.py`, re-executing only when the input dataset or script changes.

---

## PW2 - Lab A: Motion from Tracking Data

**What I did:**
- Read the noisy height measurements of a falling object (`freefall.csv`), computed velocity and acceleration with `np.gradient`, integrated the acceleration back with `cumulative_trapezoid`, and plotted position, velocity and acceleration in `motion.png`.

**Results:**
- Mean acceleration: -8.58 m/s^2 (the expected value is -9.81 m/s^2; ignoring the first and last two points gives -9.25 m/s^2)
- Standard deviation of the acceleration: 28.7 m/s^2
- Largest difference between the recovered and the original position: 0.78 m

**Why the acceleration is noisy:**
- Each derivative divides the difference between neighbouring noisy values by a small time step (0.1 s), which magnifies the measurement error, and the acceleration needs two derivatives, so it is much noisier than the position.

**What integrating back showed:**
- Even though the acceleration was very noisy, integrating it twice recovered the position to within 0.78 m, because integration is a sum and the random errors partly cancel out. Differentiation amplifies noise, integration suppresses it.

**Bonus: 2D tracked trajectory:**
- The tracked path in `trajectory.csv` has the shape of a figure eight. I computed the velocity components with `np.gradient` on x and y separately and combined them into the speed sqrt(vx^2 + vy^2); the figure is saved as `trajectory.png`.
- Max speed: 38.69, mean speed: 23.65 (position units per second). The speed rises and falls several times during the run, and the curve is a bit rough because the tracking data is noisy and the derivative amplifies that noise (only one derivative here, so much less than for the acceleration).

---

## PW2 - Lab B: Optimization in Chemistry

**What I did:**
- Compared gradient descent, Newton's method and SLSQP on two functions (`warmup.py`), then used optimization for three chemistry problems: fitting a reaction rate (`kinetics.py`), finding a chemical equilibrium (`equilibrium.py`) and locating a titration equivalence point (`titration.py`, bonus). The plots are `kinetics.png`, `equilibrium.png` and `titration.png`.

**Part 2 - Comparing the three methods:**
- Easy function f(x) = (x-3)^2 + 1: all three methods reach x = 3 (gradient descent 2.99999997, Newton 3.0, SLSQP 3.0).
- Harder function g(x) = x^4 - 3x^2 + x + 5, start x0 = 0: gradient descent (-1.3008) and SLSQP (-1.3009) reach the deep minimum (g = 1.486), but Newton stops at x = 0.170 where g'' = -5.65 < 0, so it is a maximum, not a minimum.
- Start x0 = 2: gradient descent and SLSQP again reach x = -1.30, while Newton reaches x = 1.131 with g'' = 9.35 > 0. That is a minimum, but only the shallow local one (g = 3.93).
- The starting point changed Newton's answer (0.170 vs 1.131) but not the answer of gradient descent and SLSQP. Newton solves g'(x) = 0, so it can land on a maximum or on a local minimum, and the sign of g'' must be checked. On the easy convex function the methods agree, on the harder landscape the starting point and the algorithm matter.

**Part 3 - Reaction rate:**
- Fitted rate constant: k = 0.262 (expected about 0.25). The fitted curve passes through the measured points.

**Part 4 - Chemical equilibrium (H2 + I2 <=> 2 HI, K = 15.6):**
- Newton (root-finding) and SLSQP (minimizing the squared imbalance) agree: x = 0.6638 (difference about 2e-7).
- Equilibrium amounts: H2 = 0.3362 mol, I2 = 0.3362 mol, HI = 1.3277 mol.

**Part 5 (bonus) - Titration:**
- The slope of the pH curve is largest at V = 50.0 mL, so the equivalence point is at 50.0 mL (pH = 7.0 there, largest slope 4.0 pH units per mL).