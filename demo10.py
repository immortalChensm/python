import requests

url = "http://118.24.77.117:9501/Member/User/update"
data = dict(zip(['id','name'],['4','孔子']))
print(data)

print(requests.post(url,data=data).json())