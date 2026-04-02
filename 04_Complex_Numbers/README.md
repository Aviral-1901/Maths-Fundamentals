# Imaginary Numbers
- Real numbers only allow stretching and flipping (180degree using -1) but not continuous rotation.
- We define a new axis orthogonal to real line and the unit of this axis as j.
- j is mathematical operator for a 90degree counter clockwise rotation.
- start east (+1) -> apply j(rotate 90deg) -> apply j again(rotate 180 deg)(-1)
- Applying j twice is identical to multiplying by -1
- complex number z=a+jb is a 2d coordinate packed into single algebraic entity. a is real part and b is the imaginary part.
- Multiplying two complex numbers automatically handles both scaling and rotation.


# Conjugates
- Multiplying complex numbers or just squaring them would result in another complex number.
- In real world for energy there is only real number value for energy.
- So we use conjugate of the complex number to get the real number value.
- Multiplying complex number by its conjugate gives a real number value.
- To get the conjugate we mirror the complex number to cancel the complex part of it so only the real part remains.


# Euler's Formula
- e^jθ = cos(θ) + jsin(θ)
- e^jθ represents a vector of length 1 pointing at an angle θ in complex plane.
- Instead of defining complex numbers like z = a+jb we can define them using their magnitude and phase angle z = r⋅e^jθ
- In LLMs we use e^jmθ to inject word order into transformer model and the model now can calculate relative distance between any two words by measuring angle between the vectors.


# Phasors and Wave Addition
- Handling sine waves (Acos(ωt+ϕ)) is somewhat difficult and adding them requires trignometric identities.
- To solve this problem we project 1D real wave into 2D complex plane.
- Using euler's formula e^jωt = cos(ωt)+jsin(ωt) we pretend our real oscillating wave is shadow of rotating complex vector.
- To solve the calculation with waves we factor out the part containing time (e^jωt) and do the math using the other remaining part which is simpler.
- Calculus with e^jωt is easier so it somewhat turns our calculus into algebra like d/dt becomes multiplication with jw and integration of dt becomes division with jw which allows to make maths simpler for capacitors and inductors.
