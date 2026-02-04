import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 500)
accel = np.ones(500) * 9.8
dt = t[1] - t[0]

velocity = np.cumsum(accel) * dt
position = np.cumsum(velocity) * dt
print(position)

final_v = np.trapezoid(accel, t)
print(final_v)
print(velocity[-1])

fig, axs = plt.subplots(3, 1, sharex=True, figsize=(10, 6))
axs[0].plot(t, position)
axs[0].set_title("position")

axs[1].plot(t, velocity)
axs[1].set_title("velocity")

axs[2].plot(t, accel)
axs[2].set_title("acceleration")
plt.tight_layout()
plt.show()