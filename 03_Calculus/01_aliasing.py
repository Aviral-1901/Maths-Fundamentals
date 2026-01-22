"""
Topic: Aliasing (Sampling Theory)
Scenario: Sampling a 5Hz signal with a fast sensor vs. a slow sensor.

Visualizing:
- The True Signal (High Resolution)
- The Aliased Signal (Low Resolution "Ghost")
"""

import numpy as np
import matplotlib.pyplot as plt

f_signal = 5.0
duration = 1.0

#the continuous signal, for our program 
t_high = np.linspace(0, duration, 1000)
y_high = np.cos(2 * np.pi * f_signal * t_high)

#the discrete reality, the slow sensor
#sampling rate = 7Hz 
f_sampling = 7
dt_sampling = 1.0 / f_sampling #t = 1 / f

t_slow = np.arange(0, duration, dt_sampling) #create discrete times at which we got the values
y_sampled = np.cos(2 * np.pi * f_signal * t_slow) #

plt.figure(figsize=(10,4))
plt.plot(t_high, y_high, label="True signal 5Hz", color='blue')
plt.plot(t_slow, y_sampled, 'o--', label='Sampled Data (7 Hz)', color='red')
plt.title(f"Aliasing effect: 5Hz signal sampled at {f_sampling}Hz")
plt.legend()
plt.grid(True)
plt.show()
