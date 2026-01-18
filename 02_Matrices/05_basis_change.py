"""
Topic: Change of Basis (Coordinate Transformation)
Scenario: Translating a point from Standard Coordinates to a "Tilted" VR Coordinate System.

Concept: The "Dictionary" Matrix (P)
- The columns of P are the Basis Vectors of the New System (written in Standard Language).
- P translates Alien -> Standard ( x_std = P @ x_alien ).
- To translate Standard -> Alien, we solve the system ( x_alien = P_inv @ x_std ).

Input:
- Standard Point: [10, 10]
- New Basis X: [1, 1]
- New Basis Y: [-1, 1]

Output:
- The coordinates relative to the New Basis.
"""

import numpy as np

v_std = np.array([10, 10])
P = np.array([[1, 1], [-1, 1]]).transpose()

v_alien = np.linalg.solve(P, v_std)
print("The cordinates in new grid :",v_alien)
print("For checking, standard coordinate:",P@v_alien)