"""
Topic: The Cross Product (Vector Product)
Scenario: Calculating Torque on a Quadcopter Arm.

Physics Principle: Torque (tau) = r x F
- r: Position vector (Distance from pivot to force application).
- F: Force vector (Thrust direction).
- Result: A vector perpendicular to both r and F, representing the axis of rotation.

Mathematical Constraint:
The Cross Product is strictly defined for 3D (and 7D) spaces.
- In 2D, there is no "Z-axis" for the result to point into.
- In 4D+, there is no single unique perpendicular direction (ambiguity).
- Therefore, inputs MUST be 3-element arrays, even if the Z-component is 0.
"""
import numpy as np

arm_vector = np.array([0.5, 0.0, 0.0])
thrust_vector = np.array([0.0, 0.0, 10.0])
torque = np.cross(arm_vector, thrust_vector)
print("The torque is",torque)