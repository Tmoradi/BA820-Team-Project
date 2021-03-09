# import necessary packages 
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule 
from scrapy.linkextractors import LinkExtractor
# from benchmarks.benchmarks.items import BenchmarksItem
from ..items import ScraperItem
from collections import defaultdict
import csv 


class SpiderCrawler(CrawlSpider):
    name = 'spidercrawler'

    allowed_domains = ['caring.com']
    download_delay = 5 
