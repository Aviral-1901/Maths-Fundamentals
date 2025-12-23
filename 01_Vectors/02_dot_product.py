import numpy as np

reference = np.array([1.0, 2.0, -1.0])
signal_A = np.array([1.0, 2.0, -1.0])
signal_B = np.array([-1.0, -2.0, 1.0])
signal_C = np.array([1.0, 0.0, 1.0])

def calculate_similarity(v1, v2):
    #v1 * v2 in NumPy is element-wise multiplication and np.sum gives total addition of all elements
    #valid for same-length real vector
    return np.sum(v1 * v2)  #return dot product 

reference_and_A = calculate_similarity(reference,signal_A)
reference_and_B = calculate_similarity(reference,signal_B)
reference_and_C = calculate_similarity(reference,signal_C)

print(f"Dot product of reference with signalA : {reference_and_A}, with B: {reference_and_B}, with C: {reference_and_C}")
print(np.dot(reference,signal_A)) #gives dot product
print(reference @ signal_A) #gives dot product