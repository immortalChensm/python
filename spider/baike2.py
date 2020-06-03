from pyquery import PyQuery as pq

def getHtml(url):

    html = pq(url)
    div = html(".article.block.untagged.mb15.typs_hot")

    Data = []
    for item in div.items():
        data = {}
        #print(item.find("h2").text())
        #print(item.find(".content").html())
        data['username'] = item.find("h2").text()
        data['content']  = item.find(".content").text()
        Data.append(data)
    return Data

url = "https://www.qiushibaike.com/text/"
html = getHtml(url)
for item in html:
    print(item['username']+"say:\n"+item['content']+"\n")