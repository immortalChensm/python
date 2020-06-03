import requests

url = "http://118.24.77.117:9501/Member/User/index"
params = {
    'p':2
}
result = requests.get(url,params=params)

#print(result.json())

for item in result.json():
    print(item['id'],item['name'])