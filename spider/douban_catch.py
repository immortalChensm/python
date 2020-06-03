import urllib.request
import json
import ssl


def getcontent(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    context = ssl._create_unverified_context()#类似php的curl  关闭ssl验证
    req = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(req,context=context)
    return json.loads(response.read().decode("utf-8"))


url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20'
ret = getcontent(url)
for item in ret:
    print(item['rating'],item['title'])