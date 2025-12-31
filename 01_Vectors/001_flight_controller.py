"""
Topic: Vector Operations (Addition & Scalar Multiplication)
Scenario: Calculating net force on a drone body.

Mathematical Concept: Linear Combination
Formula: F_net = (scalar * F_thrust) + F_wind

Physics Principle: Superposition of Forces.
- Scalar Multiplication scales the magnitude of the thrust.
- Vector Addition combines the independent forces (Thrust + Wind)
  into a single resultant force vector.
"""
import numpy as np

thrust = np.array([0.0, 50.0])
wind = np.array([15.0, -5.0])
scalar = 3.0

net_force = (scalar * thrust) + wind

print("The net force on a drone is:",net_force)