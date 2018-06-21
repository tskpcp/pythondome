import numpy as np
from pandas import Series,DataFrame
def indexingSelectionAndFiltering():
    print ('Series 的索引，默认数字索引可以工作')
    obj=Series(np.arange(4),index=['a','b','c','d'])
    print(obj['b'])
    print('/--------------------/')
    print(obj[3])
    print('/--------------------/')
    print(obj[[1,3]])
    print('/--------------------/')
    print(obj[obj<2])
    print('Series的数组切片')
    #闭区间
    print(obj['b':'c'])
    print('/--------------------/')
    obj['b':'c']=5
    print(obj)
    print('/****************************/')
    print('DataFrame的索引')
    data=DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colordo','Utah','New Work'],columns=['one','two','three','four'])
    print(data)
    print('/--------------------/')
    #打印列

    print(data['two'])
    print('/--------------------/')
    print(data[['three','one']])
    print('/--------------------/')
    print(data[:2])
    print('/--------------------/')
    #指定索引和列
    print(data.ix['Colordo',['two','three']])
    print('/--------------------/')
    print(data.ix[['Colordo','Utah'],[3,0,1]])
    print('/--------------------/')
    #打印第2行（从0开始）
    print(data.ix[2])
    #从开始到Utah，第2列
    print(data.ix[:'Utah','two'])
    print('根据条件选择')
    print(data[data.three>5])
    print(data<5)
    data[data<5]=5
    print(data)