# Sampling Theory and Aliasing
- Computers cannot handle continuous time. They chop the reality into Discrete Snapshots(Samples)
- Aliasing occurs when a signal oscillates faster than the sensor can track
- Nyquist-Shannon Theorem: a band-limited signal with maximum frequency f_max can be perfectly reconstructed from its samples if the sampling frequency satisfies f_s > 2 f_max
- Nyquist limit : fN = f_s / 2 -> half of the sampling frequency
- high-frequency content is misinterpreted as lower-frequency content if frequency is above the nyquist limit for a certain sampling frequency (sampling frequency fixed at first)

