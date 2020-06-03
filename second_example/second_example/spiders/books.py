# -*- coding: utf-8 -*-
import scrapy
from ..items import BooksItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com/"]
    start_urls = ['http://books.toscrape.com//']

    def parse(self, response):
        for sel in response.css("article.product_pod"):
            name = sel.xpath("./h3/a/@title").extract_first()
            price = sel.css("p.price_color::text").extract_first()
            rating = sel.css("p.star-rating").re_first("star-rating (\w+)")
            #books = {'name':name,'price':price,'rating':rating}

            books = BooksItem()
            books['name'] = name
            books['price'] = price
            books['rating'] = rating
            yield books
        url = response.css("ul.pager li.next a::attr(href)").extract_first()
        if url:
            url = response.urljoin(url)
            request = scrapy.Request(url,self.parse)
            yield request