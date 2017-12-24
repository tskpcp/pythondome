from urllib import request
import chardet
#并打印返回源文件
response=request.urlopen("http://www.jianshu.com/")
html=response.read()
charset=chardet.detect(html)
print(charset)
html=html.decode(str(charset["encoding"]))
print(html)