#!/usr/bin/python
# -*- coding:UTF-8 -*-
#coding:utf-8
#author:
#date:
#Description:爬取双色球信息收集
# https://blog.csdn.net/levy_cui/article/details/51394450
import urllib.request
from bs4 import BeautifulSoup
import os
import re


# 伪装成浏览器登陆,获取网页源代码
def getPage(href):
    headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req=urllib2.Request(url=href,headers=headers)
    try:
        post=urllib.request.urlopen(req)
    except urllib.HTTPError as e:
        print(e.code)
        print(e.reason)
    return post.read()
#初始化url 双色球首页
url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
#===============================================================================
#获取url总页数

def getPageNum(url):
    num=0
    page=getPage(url)
    soup=BeautifulSoup(page)
    strong=soup.find('td',colspan='7')

    if strong:
        result=strong.get_text().split(' ')
        list_num=re.findall('[0-9]{1}',result[1])
        for i in range(len(list_num)):
            num=num*10+int(list_num[i])
        return num
    else:
        return 0
#===============================================================================
#获取每页双色球的信息
def getText(url):
    for list_num in range(1,getPageNum(url)):
        print(list_num)
        href= 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_'+str(list_num)+'.html'
        page=BeautifulSoup(getPage(href))
        em_list=page.find_all('em')
        div_list=page.find_all('td',{'align':'center'})

        n=0
        fp=open('num.txt','w')
        for div in em_list:
            emnum1=div.get_text()
            text=div.get_text()
            text=text.encode('utf-8')
            n=n+1
            if n==7:
                text=text+'\n'
                n=0
            else:
                text=text+','
            fp.write(str(text))
        fp.close()
        fp=open('date.text','w')
        for div in div_list:
            text=div.get_text().strip('')
            list_num=re.findall('\d{4}-\d{2}-\d{2}',text)
            list_num=str(list_num[::1])
            list_num=list_num[3:13]
            if len(list_num)==0:
                continue
            elif len(list_num)>1:
                fp.write(str(list_num)+'\n')
        fp.close()
        fp01=open('date.text','r')
        a=[]
        for line01 in fp01:
            a.append(line01.strip('\n'))
        fp01.close()

        fp02=open('num.txt','r')
        b=[]
        for line02 in fp02:
            b.append(line02.strip('\n'))
        fp02.close()
        fp=open('hun.txt','a')
        for cc in zip(a,b):
            print(cc)
            fp.write(str(cc)+'\n')
        fp.close()
if __name__=='__main__':
    pageNum=getPageNum(url)
    print(pageNum)
    getPagetext=getText(url)
    print (getPagetext)
