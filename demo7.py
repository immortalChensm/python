import requests

url = "http://118.24.77.117:9501/Member/User/add"

data = {
    'name':'李师师'
}

result = requests.post(url,data=data)
print(result.json())