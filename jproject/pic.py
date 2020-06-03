import requests

url = "https://www.sxtp.net/meinv/201810/46121.html"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
res = requests.get(url,headers=headers)
res.encoding = res.encoding
print(res.text)