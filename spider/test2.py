import urllib.request
import ssl
import json

url = "https://segmentfault.com/q/1010000004954374"
headers = {
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
context = ssl._create_unverified_context()

req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req,context=context)
print(response.read().decode("utf8"))