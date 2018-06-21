import numpy as np
from pandas import DataFrame,Series
def functionApplicationAndMapping():
    print('函数')
    frame=DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
    print(frame)
    print (np.abs(frame))
    print('lambda（定义匿名函数）以及应用')
    f=lambda x:x.max()-x.min()
    print(frame.apply(f))
    print(frame.apply(f,axis=1))
    print (frame.apply(f))
    print('applymap和map')
    _format=lambda x:'%.2f'% x
    print(frame.applymap(_format))
    print(frame['e'].map(_format))