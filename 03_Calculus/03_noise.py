import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)
dt = 0.01
accel_clean = np.sin(t)
noise = np.random.normal(0, 0.02, size=len(t))
accel_noisy = accel_clean + noise

jerk_clean= np.diff(accel_clean) / dt
jerk_noisy = np.diff(accel_noisy) / dt

window_size = 15
accel_filtered = np.convolve(accel_noisy, np.ones(window_size)/window_size, mode='same')
jerk_filtered = np.diff(accel_filtered) / dt

plt.plot(jerk_clean, color='blue')
plt.plot(jerk_noisy, color='red', alpha=0.5)
plt.plot(jerk_filtered, color='green', label='Filtered')

plt.show()