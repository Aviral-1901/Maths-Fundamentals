# Day 4- matrices
- A Matrix is an operator that maps vectors from one space to another
-  Matrix multiplication translates coordinates from Local Frame(Robot Hand/Sensor) to the Global Frame(World/Desk)
- python ma pi exact hudaina ra radian ma lagda sin(pi) le exact 0 didaina tei vayera np.round() use gareko 

# matrix-chain (multiplication)
- matrix multiplication represents chaining of linear operators(matrices) from right to left
- BAx means at first x is transformed by A and resulting vector is transformed by B
- B @ A ≠ A @ B in general 
- B @ A means feed columns of A into machine B
- [A,B] is the commutator operator; it measures how sensitive the system is to the order of multiplication 
- [A,B] = AB - BA 
- if AB-BA = 0; MEANS they commute.The order of application does not matter The operations are compatible (don't interfere)
- if AB-BA != 0; MEANS they do not commute.The order matters.In quantum mechanics measuring one observable can disturb the other(basis for heisenberg uncertainity)
- two counter matrices like clockwise and counter-clock rotation by same degree about the same axis cancel the effect of each other

# determinant
- determinant gives signed area/volume scaling factor of a linear transformation.
- if determinant = 1, the volume is conserved and orientation is preserved
- if determinant >1, there was expansion of volume an if <1 then compression of volume
- if determinant = 0, then dimensions collapse, information is lost and the transformation is invertible
- if determinant is close to 0 but not exactly 0 then inverse exists but is ill-conditioned: small input errors produce large output errors, making the system numerically unstable
