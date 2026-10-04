import time
from decay import simulate, simulate_loop

N0 = 200000
LAM = 0.4

# Pure Python loop version
t0 = time.perf_counter()
simulate_loop(N0, LAM)
t1 = time.perf_counter()
loop_time = t1 - t0
print(f"Pure Python execution time: {loop_time:.4f} seconds")

# Vectorised NumPy version
t0 = time.perf_counter()
simulate(N0, LAM)
t1 = time.perf_counter()
numpy_time = t1 - t0
print(f"NumPy Vectorized execution time: {numpy_time:.4f} seconds")

print(f"NumPy is {loop_time / numpy_time:.1f} times faster")