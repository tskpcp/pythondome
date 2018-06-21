import numpy as np
from scipy import linalg

def linalgTest():
    A=np.array([[1,2],[3,4]])
    print(A)
    a=linalg.det(A)
    print(a)