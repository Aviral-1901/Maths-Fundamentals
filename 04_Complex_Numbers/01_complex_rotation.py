import numpy as np
import matplotlib.pyplot as plt

signals = np.array([1+0j, 1+0j, 1+0j, 1+0j])
shifted_signals = signals * 1j
double_shifted = shifted_signals * 1j

plt.plot(signals.real, signals.imag, 'o', color='blue', label='0 Degree shift')
plt.plot(shifted_signals.real, shifted_signals.imag, 'o', color='red', label='90 Degree shift')
plt.plot(double_shifted.real, double_shifted.imag, 'o', color='green', label='180 Degree shift')
plt.xlim(-2,2) 
plt.ylim(-2,2)
plt.grid(True)
plt.legend()
plt.show()