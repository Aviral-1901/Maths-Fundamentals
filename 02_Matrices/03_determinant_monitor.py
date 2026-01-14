import numpy as np

stateA = np.array([[2, 0], [0, 0.5]]) 
stateB = np.array([[2,1], [1, 2]])
stateC = np.array([[2,4], [1,2]])

detA = np.linalg.det(stateA)
detB = np.linalg.det(stateB)
detC = np.linalg.det(stateC)

def determinant_check(x):
    if(x==1):
        print("Volume conserved")
    elif(x>1):
        print("Expansion Detected")
    elif(np.isclose(x, 0)):
        print("System collapse")

determinant_check(detA)
determinant_check(detB)
determinant_check(detC)