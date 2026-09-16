# CSPC Computer Science for Physics and Chemistry

## PW1 - Lab A: Speed Comparison Results

* **Pure Python execution time:** 0.0147 seconds
* **NumPy Vectorized execution time:** 0.0001 seconds


## PW1 --- Lab B

### Data Analysis & Results
The observed data (`decay_observed.csv`) represents a decay process over time. Upon plotting the side-by-side comparison, the scatter points of the observed dataset match the analytical decay law ($N(t) = N_0 e^{-\lambda t}$) with $\lambda = 0.3$.

### Automation
The Snakemake pipeline automates the generation of `figure.png` from `decay_observed.csv` via `plot.py`, re-executing only when the input dataset or script changes.

## PW1 --- Lab B

![Decay Analysis](PW1/Lab%20B/figure.png)

### Data Analysis & Results
The observed data (`decay_observed.csv`) represents a decay process over time. Upon plotting the side-by-side comparison, the scatter points of the observed dataset match the analytical decay law ($N(t) = N_0 e^{-\lambda t}$) with $\lambda = 0.3$.

### Automation
The Snakemake pipeline automates the generation of `figure.png` from `decay_observed.csv` via `plot.py`, re-executing only when the input dataset or script changes.
