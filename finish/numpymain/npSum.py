
import numpy as np
import numpy.random as np_random

def npSum():
    a = np.arange(10000)**2
    b = np.arange(10000)**3
    c = a + b
    print(c)

    print('对正数求和')
    arr=np_random.randn(100)
    print((arr>0).sum())
    print('对数组逻辑操作')
    bools=np.array([False,False,True,False])
    print('有一个为Ture则返回True')
    print(bools.any())
    print('有一个为False则返回False')
    print(bools.all())