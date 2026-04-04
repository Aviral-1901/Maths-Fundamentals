import numpy as np

psi = np.array([1+1j, 2-1j])
length_squared = np.vdot(psi, psi)
norm = np.sqrt(np.real(length_squared))

psi_normalized = psi / norm
inner_product = np.vdot(psi_normalized, psi_normalized)
print(inner_product)