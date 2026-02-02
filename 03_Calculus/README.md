# Sampling Theory and Aliasing
- Computers cannot handle continuous time. They chop the reality into Discrete Snapshots(Samples)
- Aliasing occurs when a signal oscillates faster than the sensor can track
- Nyquist-Shannon Theorem: a band-limited signal with maximum frequency f_max can be perfectly reconstructed from its samples if the sampling frequency satisfies f_s > 2 f_max
- Nyquist limit : fN = f_s / 2 -> half of the sampling frequency
- high-frequency content is misinterpreted as lower-frequency content if frequency is above the nyquist limit for a certain sampling frequency (sampling frequency fixed at first)


# The Derivative(Finite Diffeence)
- In a discrete system, derivative is approximated using Finite Difference.
- The methods for this are:
- 1. Forward differece : [f(x+h) - f(x)] / h --Order of O(h) -- low accuracy
- 2. Backward difference : [f(x) - f(x-h)] / h -- Order of O(h) -- causal , used in real time
- 3. Central difference : [f(x+h) - f(x-h)] / 2h -- Order of O(h^2) -- high accuracy
- The Gradient (∇): In multi-dimensional space, the derivative becomes a vector of partial derivatives pointing in the direction of Steepest Ascent.
- Gradient Descent: The fundamental algorithm for AI training. We walk in the direction of −∇
to find the minimum error.