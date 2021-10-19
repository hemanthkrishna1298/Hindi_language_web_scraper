import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from vikaspediaSpider.items import Article
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class ArticleSpider(CrawlSpider):
    name="vikaspedia"
    allowed_domains = ['bn.vikaspedia.in']
    start_urls = [
        'https://bn.vikaspedia.in/agriculture',
        'https://bn.vikaspedia.in/sitemap',
        'https://bn.vikaspedia.in/agriculture/%E0%A6%95%E0%A7%83%E0%A6%B7%E0%A6%95%E0%A6%A6%E0%A7%87%E0%A6%B0-%E0%A6%9C%E0%A6%A8%E0%A7%8D%E0%A6%AF-%E0%A6%9C%E0%A6%BE%E0%A6%A4%E0%A7%80%E0%A6%AF%E0%A6%BC-%E0%A6%AA%E0%A6%B0%E0%A6%BF%E0%A6%95%E0%A6%B2%E0%A7%8D%E0%A6%AA%E0%A6%A8%E0%A6%BE/%E0%A6%95%E0%A6%BF%E0%A6%B8%E0%A6%BE%E0%A6%A8-%E0%A6%B0%E0%A7%87%E0%A6%B2-%E0%A6%AA%E0%A6%B0%E0%A6%BF%E0%A6%B7%E0%A7%87%E0%A6%AC%E0%A6%BE'
        ]

    rules = (
        Rule(LinkExtractor(allow = 'agriculture/'), callback='parse_item', follow = True),
    )
    
    def parse_item(self, response):

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(response.url)
        time.sleep(3)
        source = driver.page_source
        driver.quit()

        is_subfolder = source.xpath('//div/h3[@class="folder_heading"]').get()
        if not is_subfolder:
            link = response.url
            # content = response.xpath('//div[@id="texttospeak"]/text()').get()
            yield {
            'Link' : link
            }