import urllib.request

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}
url    = "http://www.baidu.com"
req = urllib.request.Request(url=url,headers=header)

response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))