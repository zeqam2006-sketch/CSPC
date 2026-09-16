
import time
import numpy as np
from decay import simulate

# Pure Python loop timing
t0 = time.time()
py_res = simulate(1000000, 0.4)
t1 = time.time()
print(f"Pure Python execution time: {t1 - t0:.4f} seconds")

# Vectorized NumPy timing
t0 = time.time()
steps = np.arange(100)
np_res = 1000000 * ((1 - 0.4) ** steps)
t1 = time.time()
print(f"NumPy Vectorized execution time: {t1 - t0:.4f} seconds")