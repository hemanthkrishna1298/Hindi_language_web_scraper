import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class NetinbagSpider(CrawlSpider):
    name="netinbag"
    allowed_domains = ['netinbag.com']
    start_urls = ['https://www.netinbag.com/hi/health-page-1.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//section[@class="pagination"]/ul/li/a'), follow = True),
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="articleList"]/li/a'), callback='parse_item', follow = False),
    )
    
    def parse_item(self, response):

        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(chrome_options=options)
        # driver.get(response.url)
        # time.sleep(3)
        # source = driver.page_source
        # driver.quit()

        # is_subfolder = source.xpath('//div/h3[@class="folder_heading"]').get()
        # if not is_subfolder:
        link = response.url
        # content = response.xpath('//div[@id="texttospeak"]/text()').get()
        yield {
        'Link' : link
        }