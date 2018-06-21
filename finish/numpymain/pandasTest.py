import pandas as pd
import numpy as np


def pandasTest():

    s=pd.Series([1,3,5,np.nan,6,8])
    print(s)

    dates=pd.date_range('20180517',periods=6)
    print(dates)

    df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
    print(df)
    print('从头部开始输出行数：df.head()')
    print(df.head(1))
    print('从底部开始输出行数：df.tail()：')
    print(df.tail(2))
    print('计算性能值：df.describe()')
    print(df.describe())
    print('行列转至：df.t：')
    print(df.T)
    print('排序：df.sort_values()：')
    print(df.sort_values(by='B'))
    df.sort_values(by='B')