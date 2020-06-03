import urllib.request
import urllib.parse
import json


poststr = {
    "a":"jack",
    "b":"tom"
}
url = "http://118.24.77.117:9501/admin/Index/postjson"
postData = urllib.parse.urlencode(poststr).encode("utf-8")
req = urllib.request.Request(url=url,data=postData)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
