"""
a = 0x55
b = 0xaa

print(a|b)
result = requests.post(url,data=data,params=params,cookies=cookies)
print(result.text)
result = requests.get(url,cookies=cookies)
print(result)
cookies = dict(name='tom')

result = requests.post(url,files={"file":open("demo3.py","rb")})
print(result.status_code)
print(result.text)
result = requests.get(url,params={'name':'tony'})
print(result.text)

result = requests.get(url,params=params)
print(result.text)
"""
import requests

url = "http://118.24.77.117:9501/test/demo2?a=b";
header = {
    "Cookie":"jklsjlfakjlfjskldf"
}
data = {
    'name':'jackcsm',
    'age':'100'
}
params ={
    'type':'a'
}

print(requests.post(url,data=data).text)