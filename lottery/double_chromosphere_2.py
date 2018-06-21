import urllib.request
import urllib.parse
import re
import http.cookiejar
# https://www.cnblogs.com/zdz8207/p/python_learn_note_14.html
def getHtml(url):
    cj=http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
                         ('Cookie', '4564564564564564565646540')]
    urllib.request.install_opener(opener)
    html_bytes=urllib.request.urlopen(url).read()
    html_string=html_bytes.decode('utf-8')
    return html_string

def doubleChromosphere2():
    url='http://zst.aicai.com/ssq/openInfo/'
    html=getHtml(url)
    table=html[html.find('<table class="fzTab nbt">'):html.find('</table>')]
    tmp = table.split('<tr \r\n\t\t                  onmouseout=', 1)

    trs=tmp[1]
    tr=trs[: trs.find('</tr>')]
    number = tr.split('<td   >')[1].split('</td>')[0]
    print(number+'期开奖号码：')
    redtmp=tr.split('<td class="redColor sz12">')
    reds=redtmp[1:len(redtmp)-1]


    print(reds)
    for redstr in reds:
        print(redstr.split('</tr>')[0]+",")
    print('篮球:')
    blue = tr.split('<td  class="blueColor sz12" >')[1].split('</td>')[0]
    print(blue)
