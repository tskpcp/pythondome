
def get_mobile(phone):
    import requests
    from lxml import etree
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url='https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile'

    req=requests.get(url,headers=headers)
    req.encoding='utf-8'
    e=etree.HTML(req.text)
    print(e.xpath())
    datas=e.xpath('//tr/td[2]/span/text()')
    print(datas)
get_mobile(15811122861)