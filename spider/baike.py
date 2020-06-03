import urllib.request
import json
import ssl
import re

def getcontent(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf8")
    pattern = r'<div class="article block untagged mb15 typs_hot" id="qiushi_tag_120596283">(.*?)'
    re_joke = re.compile(pattern,re.S)
    joke = re_joke.findall(data)

    print(joke)

url = "https://www.qiushibaike.com/text/"
getcontent(url)