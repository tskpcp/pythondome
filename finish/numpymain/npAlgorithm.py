
import numpy as np
import numpy.random as np_random

    #索引原理，切片原理
def  npAlgorithm():
    print('求平方根')
    arr=np.arange(10)
    print(np.sqrt(arr))
    print('数组比较')
    x=np_random.randn(8)
    y=np_random.randn(8)
    print('x=',x)
    print('y=',y)
    print(np.maximum(x,y))
    print('使用modf函数把浮点数分解成整数和小数部分')
    print('统一乘5')
    arr=np_random.randn(7)*5
    print(np.modf(arr))
