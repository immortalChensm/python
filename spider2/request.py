from scrapy import Request
import scrapy
import json
def parse(response):
    print(json.loads(response.text))

req = Request('http://httpbin.org/anything',callback=parse)

