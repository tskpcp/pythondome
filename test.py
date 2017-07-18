import numpy as np
def pySum():
    a=list(range(10000))
    b=list(range(10000))
    c=list()
    for i in range(len(a)):
        c.append(a[i]**2+b[i]**2)
    return c

def npSum():
    a = np.arange(10000)**2
    b = np.arange(10000)**3
    c = a + b
    return c
