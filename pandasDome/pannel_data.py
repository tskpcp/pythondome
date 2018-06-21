import numpy as np
import pandas as pd
import pandas_datareader as web
from pandas import Series,DataFrame,Index,Panel
def pannelData():
    pdata=Panel(dictr((stk,web.DataReader(stk,'1/5/2018','30/5/2018')) for stk in['F-F_Research_Data_factors','famafrench']))
    print(pdata)
    pdata=pdata.swapaxes('items','minor')
    print(pdata)

    print('访问顺序：item->major->minor')
    print(pdata['Adj Close'])
    print(pdata[:,'15/5/2018',:])
    print(pdata['Adj Close','16/5/2018',:])

    print('Panel与DataFrame相互转换')
    stacked=pdata.ix[:,'17/5/2018',:]
    print(stacked)
    print (stacked.to_panel())