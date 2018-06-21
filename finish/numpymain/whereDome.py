
import numpy as np


def whereDome():
    print('通过真值表选择元素')
    x_arr=np.array([1.1,1.2,1.3,1.4,1.5])
    y_arr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond=np.array([True,False,True,True,False])

    print('通过列表推')
    result=[(x if c else y) for x,y,c in zip(x_arr,y_arr,cond)]
    print(result)
    print('使用Numpy的where函数')
    print(np.where(cond, x_arr, y_arr))
    print('更多where函数')
    arr=np_random.randn(4,4)
    print(arr)
    print(np.where(arr>0,2,-2))
    print(np.where(arr>0,2,arr))
    print('where嵌套')
    cond_1=np.array([True,False,True,True,False])
    cond_2=np.array([False,True,False,True,False])
    print('传统代码')
    result=[]
    for i in range(len(cond)):
        if cond_1[i] and cond_2[i]:
            result.append(0)
        elif cond_1[i]:
            result.append(1)
        elif cond_2[i]:
            result.append(2)
        else:
            result.append(3)
    print(result)
    print('np版本代码')
    result=np.where(cond_1 & cond_2,0, np.where(cond_1,1,np.where(cond_2,2,3)))
    print(result)