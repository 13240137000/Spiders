# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
from Spiders.items import DangDangItem


class DangDangSpider(scrapy.Spider):

    name = 'dangdang'
    allowed_domains = ['dangdang.com']

    __protocol = ""
    __port = ""
    __keyword = ""

    base_url = "{}://search.dangdang.com:{}/?key={}&act=input"

    def __init__(self, keyword=None, protocol=None, port=None, *args, **kwargs):

        if keyword is not None:
            self.__keyword = keyword
        else:
            self.__keyword = "python"

        if protocol is not None:
            self.__protocol = protocol
        else:
            self.__protocol = "http"

        if port is not None:
            self.__port = port
        else:
            self.__port = "80"

    def start_requests(self):

        url = self.base_url.format(self.__protocol, self. __port, self.__keyword)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        try:

            log.msg("Your has been enter callback method.", level=log.INFO)

            extract_collection = {
                "root": "div[id='search_nature_rg'] > ul.bigimg > li",
                "title": "p.name a::attr(title)",
                "detail": "p.detail::text",
                "now_price": "p.price > span.search_now_price::text",
                "pre_price": "p.price > span.search_pre_price::text",
                "discount": "p.price > span.search_discount::text",
                "author": "p.search_book_author > span > a[dd_name='单品作者']::text",
                "publish": "p.search_book_author > span > a[dd_name='单品出版社']::text",
                "publish_date": "p.search_book_author > span:nth-of-type(2)::text",
                "star": "p.search_star_line > span.search_star_black > span::attr(style)",
                "comment": "p.search_star_line > a.search_comment_num::text",
                "next_request": "div.paging > ul > li.next > a::attr(href)"
            }

            for el in response.css(extract_collection["root"]):
                item = DangDangItem()
                item["title"] = el.css(extract_collection["title"]).extract_first() if el.css(extract_collection["title"]).extract_first() is not None else ""
                item["detail"] = el.css(extract_collection["detail"]).extract_first() if el.css(extract_collection["detail"]).extract_first() is not None else ""
                item["now_price"] = el.css(extract_collection["now_price"]).extract_first() if el.css(extract_collection["now_price"]).extract_first() is not None else ""
                item["pre_price"] = el.css(extract_collection["pre_price"]).extract_first() if el.css(extract_collection["pre_price"]).extract_first() is not None else ""
                item["discount"] = el.css(extract_collection["discount"]).extract_first() if el.css(extract_collection["discount"]).extract_first() is not None else ""
                item["author"] = el.css(extract_collection["author"]).extract_first() if el.css(extract_collection["author"]).extract_first() is not None else ""
                item["publish"] = el.css(extract_collection["publish"]).extract_first() if el.css(extract_collection["publish"]).extract_first() is not None else ""
                item["publish_date"] = el.css(extract_collection["publish_date"]).extract_first() if el.css(extract_collection["publish_date"]).extract_first() is not None else ""
                item["star"] = el.css(extract_collection["star"]).extract_first() if el.css(extract_collection["star"]).extract_first() is not None else ""
                item["comment"] = el.css(extract_collection["comment"]).extract_first() if el.css(extract_collection["comment"]).extract_first() is not None else ""

                yield item

            next_request_link = response.css(extract_collection["next_request"]).extract_first()

            if next_request_link:
                url = response.urljoin(next_request_link)
                yield scrapy.Request(url=url, callback=self.parse)

                log.msg("requested next page.", level=log.INFO)

        except Exception as error:
            log.msg(error, level=log.ERROR)
