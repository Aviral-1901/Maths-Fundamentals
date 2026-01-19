"""
Topic: Eigenvalues and Stability Analysis
Scenario: Determining if a drone control system will crash.

Concept: 
- Discrete Time System: x(t+1) = A * x(t)
- Stability condition: Magnitude of ALL eigenvalues must be < 1.
- If |lambda| > 1, the state vector grows exponentially (Explosion).
"""

import numpy as np

matrixA = np.array([[0.5, 0], [0, 0.8]])
matrixB = np.array([[1.1, 0], [0, 0.9]])

evalsA, evecsA = np.linalg.eig(matrixA)
evalsB, evecsB = np.linalg.eig(matrixB)

resultA = np.all(np.abs(evalsA) < 1)
resultB = np.all(np.abs(evalsB) < 1)

if resultA:
    print("System A is stable")
else:
    print("system A is unstable")

if resultB:
    print("System B is stable")
else:
    print("System B is unstable")