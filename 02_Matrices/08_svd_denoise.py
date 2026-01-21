"""
Topic: SVD Application (Noise Reduction / Denoising)
Scenario: Recovering a clean signal (Vertical Stripe) from a noisy image.

Method: Truncated SVD (Low-Rank Approximation).
1. The Clean Signal is Rank 1 (Simple structure).
2. The Noise is Full Rank (Random static everywhere).
3. SVD separates them: Large Sigma = Signal, Small Sigma = Noise.
4. By setting small Sigma values to 0, we delete the noise mathematically.

Variables:
- clean_data: The perfect 10x10 image.
- dirty_data: Image + Random Noise.
- S_clean: The filtered singular values (only the top 1 is kept).
"""

import numpy as np

clean_data = np.zeros((10, 10))

clean_data[:, 4] = 1
noise = 0.1 * np.random.rand(10, 10)
dirty_data = clean_data + noise

U, S, Vt = np.linalg.svd(dirty_data)
S_clean = S.copy()

S_clean[1:] = 0

cleaned_data = U @ np.diag(S_clean) @ Vt

print(cleaned_data[0][0])
print(dirty_data[0][0])

