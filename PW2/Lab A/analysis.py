"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)
print("Mean acceleration:", a.mean())
print("Std of acceleration:", a.std())
print("Mean acceleration without edge points:", a[2:-2].mean())

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]
max_diff = np.max(np.abs(y_rec - y))
print("Max difference between recovered and original position:", max_diff)

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 9))

axes[0].plot(t, y)
axes[0].set_ylabel("Position (m)")
axes[0].set_title("Free fall from tracking data")

axes[1].plot(t, v)
axes[1].set_ylabel("Velocity (m/s)")

axes[2].plot(t, a, label="acceleration from data")
axes[2].axhline(-9.81, color="red", linestyle="--", label="-9.81 m/s^2")
axes[2].set_ylabel("Acceleration (m/s^2)")
axes[2].set_xlabel("Time (s)")
axes[2].legend()

plt.tight_layout()
plt.savefig("motion.png", dpi=150)

# ---------- Bonus: 2D tracked trajectory ----------
traj = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
tt = traj[:, 0]
x2 = traj[:, 1]
y2 = traj[:, 2]

vx = np.gradient(x2, tt)
vy = np.gradient(y2, tt)
speed = np.sqrt(vx**2 + vy**2)

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

ax1.plot(x2, y2)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("Tracked path (x vs y)")

ax2.plot(tt, speed)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Speed")
ax2.set_title("Speed over time")

plt.tight_layout()
plt.savefig("trajectory.png", dpi=150)
print("Max speed:", speed.max())
print("Mean speed:", speed.mean())
