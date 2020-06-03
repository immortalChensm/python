import urllib.request
import os
from pyquery import PyQuery as pq
import re
import ssl
import collections

def writeFile(html,file,type='w'):
    with open(file,type) as f:
        f.write(html)
    f.close()

def getHtml(url,file):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(req,context=context)
    #print(response.read().decode("utf8"))
    data = response.read().decode("utf8")
    doc = pq(data)
    qqstr = doc(".clearfix.comment-item").find("p").text()
    qqstr_pattern = r'([1-9][0-9]{4,14})'
    re_qq = re.compile(qqstr_pattern)
    qqList = re_qq.findall(qqstr)
    #获取qq并去重 集合：元素不得重复
    qqList = list(set(qqList))

    #获取本页的链接  用于再次获取
    page = doc(".paginator")
    a = page.find("a")

    pageList = []
    for item in a.items():
        pageList.append(item.attr.href)

    #print(qqList)
    #将内容写入文件里
    if len(qqList):
        with open(file,"a") as f:
            for qq in qqList:
                f.write(qq+"\n")
        f.close()

    pageList = list(set(pageList))
    return pageList




def centerController(url,file):
    #初始队列
    dequee = collections.deque()
    #进队
    dequee.append(url)
    while len(dequee)!=0:
        #出队
        tempUrl = dequee.popleft()
        #url = "https://www.douban.com/group/topic/17359302/"
        #爬取数据，返回链接说明还有数据，直到最后一页为止
        pageList = getHtml(tempUrl,file)
        for page in pageList:
            dequee.append(page)

url = "https://www.douban.com/group/topic/17359302/"
file = "file/qq.txt"
centerController(url,file)

