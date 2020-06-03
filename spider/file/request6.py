import urllib.request


for i in range(1,100):

    try:
        response = urllib.request.urlopen("http://www.baidu.com", timeout=0.1)
        print(len(response.read()))
    except:
        print("超时，爬取失败")

