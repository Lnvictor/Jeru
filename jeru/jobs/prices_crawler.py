import threading
from threading import Thread

import scrapy
from scrapy.crawler import CrawlerProcess

from utils import load_from_csv, parse_enxuto, parse_higa


class EnxutoSpider(scrapy.Spider):
    name = "enxuto"

    start_urls = {"https://enxuto.com.br/mercearia"}

    def parse(self, response):
        parse_enxuto(response)


class HigaSpider(scrapy.Spider):
    name = "higa"

    start_urls = {"https://www.higa.com.br/"}

    def parse(self, response):
        parse_higa(response)


class PricesCrawler:
    spider_settings = {}

    def run_crawler(self):
        process = CrawlerProcess(self.spider_settings)
        process_2 = CrawlerProcess(self.spider_settings)
        process.crawl(EnxutoSpider)
        process_2.crawl(HigaSpider)
        t1 = Thread(target=process.start)
        t2 = Thread(target=process_2.start)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        load_from_csv()
