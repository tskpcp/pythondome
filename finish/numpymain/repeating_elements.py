import numpy as np
import numpy.random as np_random
def repeatingElements():
    print('Repeat：按元素')
    arr=np.arange(3)
    print(arr)
    print(arr.repeat(3))
    print('3个元素，分别复制2,3,4次，长度要匹配')
    print(arr.repeat([2,3,4]))
    print('Repeat：制定轴')
    arr=np_random.randn(2,2)
    print(arr)
    print(arr.repeat(2,axis=0))
    print(arr.repeat(2,axis=1))
    print('Tile:参考贴瓷砖')
    print(np.tile(arr,2))
    print(np.tile(arr,(2,3)))
