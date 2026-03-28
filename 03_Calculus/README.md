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

# Differentiation Amplifies Noise
- Numerical differentiation acts as high pass filter.
- In frequency domain, differentiating n times is equivalent to multiplying the signal's spectrum by (jω)^n
- Tiny high frequency jitters in position result in massive spikes in velocity.
- As the sampling interval gets smaller, the noise amplification gets larger.
- Never differentiate raw sensor data. [Signal -> Low Pass filter(smooth) -> Differentiate]


# Numerical Integration
- Integration is mathematical accumulation of values over time. In discrete system, we approximate the area under the curve by summing discrete slice (y⋅Δt)
- Integral has infinite memory meaning the contents added stay there.
- Every error or small drift from a sensor is added to the total and saved forever. This leads to integration drift. A tiny constant bias in acceleration results in a position error that grows with time squared.


# Partial Derivative and Jacobian
- Partial derivative is a measurement of change that ignores everything except one variable.
- When calculating ∂/∂x of an equation, treat other variables (y, z) as constants.
- Jacobian is a matrix that maps many inputs to many outputs.
- Columns of jacobian represents inputs and rows represents outputs.
- Slot(i,j) tells how much output i changes if changed the input j.


# Gradient
- Gradient is a vector which is composed of all partial derivatives.
- Gradient always points in the direction of steepest ascent.
- Gradient is always perpendicular to contour lines of the function.
- Contour lines are those where f(x,y) = constant. Walking along this line causes zero altitude change.The gradient is always perpendicular to contour lines.
- The length of gradient vector represents the maximum rate of change at that point.


# Chain Rule
- Chain rule allows for calculation of derivative of nested functions.
- It helps to see how the output is affected by each variables in the chain.
- If change flows through a chain (A -> B -> C), multiply the local gradients.
- If a variable affects the output through different independent paths, we add the gradients of those paths.


# Gradient Descent
- Iterative optimization algorithm used to find the local minimum of a differentiable function
- θn+1 = θn − α∇J(θn)
- j(θ) : The loss function(Error) and α : the learning rate
- we move in direction of negative gradient because gradient always points uphill.
- As we move near the bottom, the slope(gradient) naturally shrinks causing the algorithm to take smaller, more precise steps.
- convex function : only one global minimum. Easy to solve
- Non-convex function : multiple local minima and saddle points.