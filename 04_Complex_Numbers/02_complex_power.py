import numpy as np

signal = np.array([3.0 + 4.0j, 0.0 + 5.0j, -2.0 - 2.0j])
signal_conj = np.conj(signal)

power = signal * signal_conj
power_clean = np.real(power)

power_clean2 = np.abs(signal)**2

print(power_clean)
print(power_clean2)