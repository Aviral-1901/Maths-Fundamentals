import numpy as np

def normalize(vect):
    v = np.array(vect, dtype=complex)  # Converts input list into a NumPy array of complex numbers
    #dtype = complex -> Reserve enough memory for Real and Imaginary parts for every slot, even if the current numbers look simple.

    squared_components = v * np.conj(v)
    squared_sum = np.real(np.sum(squared_components)) #converts squared sum into real numbers as v*np.conj(v) garda output complex auxa like 4+0j
    magnitude = np.sqrt(squared_sum)
    return v / magnitude

raw_vector = [2, -3j, 1+2j]
print(f"Original vector is {raw_vector}")

norm_vector = normalize(raw_vector)
print(f"Normalized vector is {norm_vector}")

norm_vector_mag = np.linalg.norm(norm_vector)  #to find magnitude of vector we use np.linalg.norm()
print("Normalized magnitude is",norm_vector_mag)