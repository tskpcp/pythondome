import urllib
def gethtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html