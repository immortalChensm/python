import urllib.request
import urllib.parse

url = "http://www.baidu.com"

#response = urllib.request.urlopen(url)
#print(response.read().decode("utf-8"))

url = "http://www.itkucode.com/demo/mall/home/index/testcsm"

post = {
    "name":"jack",
    "age":1000
}

postStr = urllib.parse.urlencode(post).encode("utf8")
req = urllib.request.Request(url,data=postStr)

response = urllib.request.urlopen(req)
print(response.read().decode("utf8"))
print(response.info())
print(response.getcode())