import numpy as np
import matplotlib.pyplot as plt

f = 100
omega = 2 * np.pi * f
t = np.linspace(0, 0.05, 500)

v_noise = 5.0 * np.exp(1j * np.radians(45))
v_anti = 5.0 * np.exp(1j * np.radians(225))
v_total = v_noise + v_anti

wave_noise = np.real(v_noise * np.exp(1j * omega * t))
wave_anti = np.real(v_anti * np.exp(1j * omega * t))
wave_total = np.real(v_total * np.exp(1j * omega * t))

plt.plot(t, wave_noise, color='red', label='noise')
plt.plot(t, wave_anti, color='blue', label='anti')
plt.plot(t, wave_total, color='green', label='total')
plt.legend()
plt.grid(True)
plt.show()