import numpy as np
import numpy.random as np_random
def fancyIndexingEquivalents():
    print('Fancy Indexing')
    arr=np.arange(10)*100
    inds=[7,1,2,6]
    print(arr)
    print(arr[inds])
    print('使用take')
    print(arr.take(inds))
    print('使用put更新内容')
    arr.put(inds,50)
    print(arr)
    arr.put(inds,[70,10,20,60])
    print(arr)
