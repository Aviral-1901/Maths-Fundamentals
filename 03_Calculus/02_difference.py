import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 20)
x = t ** 3

dt = t[1] - t[0]
# velocity = np.diff(x) / dt
# t_v = t[:-1]
velocity = np.gradient(x, dt)

# acceleration = np.diff(velocity) / dt
# t_a = t_v[:-1]
acceleration = np.gradient(velocity, dt)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(6, 8))

#Position
ax1.plot(t, x, 'o-', color='blue')
ax1.set_ylabel('Position (m)')
ax1.set_title('Motion Analysis')

#Velocity
ax2.plot(t, velocity, 'o-', color='green')
ax2.set_ylabel('Velocity (m/s)')

#Acceleration
ax3.plot(t, acceleration, 'o-', color='red')
ax3.set_ylabel('Accel (m/s^2)')
ax3.set_xlabel('Time (s)')

plt.tight_layout()
plt.show()