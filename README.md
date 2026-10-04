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

## PW1 --- Lab B

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