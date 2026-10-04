# CSPC Computer Science for Physics and Chemistry

## PW1 - Lab A: Speed Comparison Results

* **Pure Python execution time:** 0.0147 seconds
* **NumPy Vectorized execution time:** 0.0001 seconds

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