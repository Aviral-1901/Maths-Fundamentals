import numpy as np

key = np.array([1.0, 5.0, 2.0])
scan_valid = np.array([1.0, 5.0, 2.0])
scan_intruder = np.array([-1.0, -2.0, 1.0])
scan_noise = np.array([5.0, -1.0, 0.0])

valid = key @ scan_valid
intruder = key @ scan_intruder
noise = key @ scan_noise

print(f"Valid one's score: {valid}, intruder's score: {intruder}, noise's score: {noise}")