import urllib.request
import json

url = "http://118.24.77.117:9501/admin/Index/getjson"

response = urllib.request.urlopen(url,timeout=0.5)

#print(response.read())
#print(response.read().decode("utf-8"))
data = response.read().decode("utf-8")
#print(type(data))
#jsonStr = '{"name":"jackcsm","age":18,"facev":100,"money":10000000000}'
#print(type(jsonStr))
jsonData = json.loads(data)
print(jsonData)
print(type(jsonData))
print(jsonData['name'])

jsonStr2 = json.dumps(jsonData)
print(type(jsonStr2))
print(jsonStr2)