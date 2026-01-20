"""
Topic: SVD Rank Detection
Scenario: Determining if 2D sensor data is actually 1D signal + noise.

Logic:
1. Decompose Matrix A using SVD.
2. Inspect Singular Values (S).
3. If S[0] >> S[1] (Condition Number is huge), the data is Rank 1 (Line).
   If S[0] ~ S[1], the data is Rank 2 (Blob).
"""

import numpy as np

A = np.array([[2, 4], [1, 2.01]])

# Compute SVD
# U: Output Rotation
# S: List of Stretch Factors [sigma1, sigma2]
# Vt: Input Rotation
U, S, Vt = np.linalg.svd(A)

print(S)

condition_number = S[0] / S[1]
print(condition_number)