import requests

url = "http://118.24.77.117:9501/Member/User/delete"

data = dict(id=5)

print(requests.post(url,data=data).json())