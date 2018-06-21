# import numpy as np
# import pandas_datareader.data as web
# from pandas import Series,DataFrame
# def correlationAndCovariance():
#     all_data={}
#     for ticker in['AAPL','IBM','MSFT','GOOG']:
#         all_data[ticker]=web.get_data_yahoo(ticker,'4/1/2016','7/15/2016')
#         price=DataFrame({tic:data['Adj Close'] for tic,data in all_data.iteritems()})
#         volume=DataFrame({tic:data['Volume'] for tic,data in all_data.iteritems()})
#     returns=price.pct_change()
#     print(returns.tail())
#     print(returns.MSFT.corr(returns.IBM))
#     print(returns.corr())
#     print (returns.cov())
#     print (returns.corrwith(returns.IBM))
#     print (returns.corrwith(returns.volume))