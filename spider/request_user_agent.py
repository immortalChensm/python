import urllib.request
import random
headers = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
]
#随机选择一个请求客户端信息  防止封ip
agentStr = random.choice(headers)
url = "http://www.baidu.com"
req = urllib.request.Request(url=url)
req.add_header("User-Agent",agentStr)

response = urllib.request.urlopen(req)
print(response.info())
print(response.read().decode("utf-8"))