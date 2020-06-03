import urllib.request


url = "http://www.baidu.com"

newurl = urllib.request.quote(url)
print(newurl)

url2 = urllib.request.unquote(newurl)
print(url2)

response = urllib.request.urlopen(url2)
print(response.read())