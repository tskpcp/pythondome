import urllib.request
import urllib.parse
import numpy as np
import http.cookiejar
import pandas as pd
from bs4 import BeautifulSoup
from pandas import DataFrame

def doubleChromosphereWy():
    data=getYear()
    #print(data)
    header=titles('http://trend.caipiao.163.com/ssq/?year=2004')
    print(len(data))
    print(len(header))
    pd.set_option('max_rows',len(data))
    pd.set_option('max_columns',len(header))
    df=pd.DataFrame(data,columns=header)
    print(df)

def getYear():
    list_years = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    #list_years = [2004,2005]
    data=[]
    for item in list_years:
       data+=wangyi(item)
    return data

def wangyi(year):
    url='http://trend.caipiao.163.com/ssq/?year='+str(year)
    html = getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    #单元格内容
    tr=soup.table.tbody.find_all('tr')
    data_list=[]
    for data in tr:
        idata=data.get('data-period')
        bull=[int(idata)]
        for item in data.find_all('td'):
            foldcolor=item.get('class')
           #红球
            if foldcolor==['f_red'] or foldcolor == ['f_blue']:
                 # print('0')
                  bull.append(0)
            if foldcolor==['ball_brown']or foldcolor==['ball_red'] or foldcolor==['ball_blue', 'js-fold']:
                 # print(item.get_text())
                  bull.append(int(item.get_text()))
        data_list.append(bull)
    #print(data_list)
    return data_list

def titles(url):
    html = getHtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    # 列名
    thead = soup.table.thead.tr.stripped_strings
    column_list = []
    for th in thead:
        column_list.append(th)
    return column_list

def getHtml(url):
    cj=http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
                         ]
    urllib.request.install_opener(opener)
    html_bytes=urllib.request.urlopen(url).read()
    html_string=html_bytes.decode('utf-8')
    return html_string
