import scrapy
from scrapy.spiders import CrawlSpider , Spider 
from scrapy.spiders import Rule 
from scrapy.linkextractors import LinkExtractor
# from benchmarks.benchmarks.items import BenchmarksItem
from ..items import ScraperItem
from collections import defaultdict
import csv 

class Scraper(Spider):
    name = 'spider'

    # adding an instance of our 
    # db_client = MongoDB()
    # where to start scrapings
    # only accept certain links to traverse through 
    # only want to go through sjc opinion text
    # allowed_domains = ['caring.com']
    # # going to read in the file 
    # download_delay = 5

    start_urls = [
        'https://www.caring.com/senior-living/california/lynwood/california-post-acute-care'
    ]
    # file = open('C:/Users/tiamm/Desktop/benchmarks/benchmarks/benchmarks/urls/urls.csv')
    # start_urls = [line.strip() for line in file]

    
    # tells scrapy which function to use when parsing the Response 
    # object it get back after requesting the content of the links it 
    # finds insider the xpath we give it
    # custom_settings = {
    #     'DEPTH_LIMIT': 5,
    #     'Download_DELAY': 5
    # }

    # rules = (
    #     Rule(LinkExtractor(allow=(),restrict_xpaths = ('//tr/td/a')) ,
    #     callback = 'parse_items',follow=True),
    # )
    
    # def extract_data(self,response,type):
    #     ''' type either needs to be 'case','headnote', or 
    #         'text'
    #     '''
    #     if type == 'case':
    #         data_ = response.xpath('////header[@class="w3-container"]/h1/text()').extract()
    #     elif type == 'headnote':
    #         response.xpath('//secton[@class="headnote"]/p/text()').extract()
    #     else:
    #         data_ = response.xpath('//secton[@class="opinion"]/p/text()').extract()
    #     data_ = [value.lstrip().rstrip() for value in data_]
    #     return data_
    
    # def parse_cases(self,response):
    #     # getting the title, headnote, and opinion of the 
    #     # case, also going to preprocess the 
    #     item = Ba820Item(
    #         case=self.extract_data(response,'case'),
    #         headnote=self.extract_data(response,'headnote'),
    #         text=self.extract_data(response,'text'))
    #     yield item 




    def parse(self,response):
        items = ScraperItem()
        # nursing_home_address = response.xpath('/html/body/main/article/div/div/div[4]/div/div[2]/div[1]/text()').extract()
        # nursing_home_name = response.xpath('/html/body/main/article/div/div/div[4]/div/div[1]/div[1]/h1').extact()
        nursing_home_reviews = response.xpath('//div[@class="body-text"]/div[@class="description"]/text()').extract()
        medical_number = response.xpath('//ul[@class="list-unstyled"]/li/span[@class="value"]/a/text()').extract()
        name = response.xpath('//div[@class="col-md-6 left"]/div/h1/text()').extract()
        # nursing_home_review_stars = response.xpath('//i[@class="far fa-star"]').extract()

        # items['name'] = nursing_home_name
        # items['address'] = nursing_home_address 
        items['review'] = nursing_home_reviews
        items['medical_number'] = medical_number
        items['name'] = name
        # items['score'] = nursing_home_review_stars 

        yield items