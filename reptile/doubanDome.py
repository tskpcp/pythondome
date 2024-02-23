#爬取豆瓣出版社信息
import urllib.request
import re

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
url="https://read.douban.com/provider/all"
address="C:\\Users\\tskpc\\Desktop\\"
req=urllib.request.Request(url,headers=headers)

# data=urllib.request.urlopen(req).read().decode('utf-8')
# pat='<div class="name">(.*?)</div>'
# rst=re.compile(pat).findall(data)
# fh=open("C:\\Users\\tskpc\\Desktop\\chubanshe.txt","w")
# for i in range(0,len(rst)):
#     print(rst[i])
#     fh.write(rst[i]+"\n")
# fh.close()


# urlretrieve(网址，本地文件存储地址) 直接下载网页到本地
#urllib.request.urlretrieve(url,"C:\\Users\\tskpc\\Desktop\\dd.html")
# urlcleanup()
# getcode()
# info()

keywd="python"
keywd=urllib.request.quote(keywd)
url="https://www.baidu.com/s?wd="+keywd
req=urllib.request.Request(url,headers=headers)
data=urllib.request.urlopen(req).read().decode('utf-8')
print(data)
pat="title:'(.*?)',"
rst=re.compile(pat).findall(data)
print(rst)