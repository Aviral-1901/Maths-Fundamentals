import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)
omega = 2 * np.pi * 3
Z = np.exp(1j * omega * t)

plt.plot(t, Z.real, color='blue', label='Real(cosine)')
plt.plot(t, Z.imag, color='red', label='Imaginary(sine)')
plt.show()