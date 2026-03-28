import numpy as np

x, y = 10.0, 10.0
alpha = 0.1
iterations = 100
history = []

#z = x^2 + y^2
for i in range(iterations):
    grad_x = 2*x
    grad_y = 2*y
    x = x - alpha * grad_x
    y = y - alpha * grad_y
    history.append([x, y])

print(history)