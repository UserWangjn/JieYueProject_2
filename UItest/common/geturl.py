def GetUrl(url):
    urls=url.split('/')
    url=urls[0]+'/'+urls[1]+'/'+urls[2]+'/'+urls[3]
    return url
#testurl=GetUrl('https://www.baidu.com/')
#testurl=GetUrl('http://172.18.100.89:8080/core-web')
#print(testurl)