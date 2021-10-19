from bs4 import BeautifulSoup
import requests
import os
import json
import re
import ssl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

gcontext = ssl.SSLContext()
# use header if access is denied.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
# agent = {"User-Agent":"Mozilla/5.0"}

# def ignore_english(text):
#     """
#     Function takes in multi-language text and returns text without the english part in it.
#     """
#     text = ''.join(i for i in text if ord(i)<65 or (ord(i)<97 and ord(i)> 90) or ord(i)>122)
#     text = " ".join(text.split())
#     return text

link = "https://www.netinbag.com/hi/finance/what-is-wholesaling.html"


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)
driver.get(link)
time.sleep(3)
source = driver.page_source
driver.quit()


# source = requests.get(link, headers = headers).text

soup = BeautifulSoup(source, "lxml")
# print(soup.prettify)
#scraped_text_list = []
# relevant_content = (((soup.body.find('tr')).find_all('tr'))[2]).find_all('tr')[2]
# print(relevant_content_1.prettify)
# relevant_content = soup.body.find('section', class_="article-detail auw-lazy-load")
# relevant_content2 = relevant_content.find_all('div', class_= "CssComponent-sc-1oskqb9-0 cXjXFI")
relevant_content = soup.body.find('article', id="fullArticle")
# print(relevant_content)
# if(relevant_content==None):
    # relevant_content = soup.body.find('section', class_="lead-gallery auw-lazy-load")
#for para in relevant_content:
scraped_text_list = []
for para in relevant_content.find_all('p'):
    scraped_text = para.get_text()
    if(len(scraped_text)>0):
        scraped_text_list.append(scraped_text)
    scraped_text = ""
    scraped_text = scraped_text.join(scraped_text_list)

# if(len(text)>0):
#     scraped_text_list.append(text)
# scraped_text = ""
# scraped_text = scraped_text.join(scraped_text_list)
with open(os.path.join('hello'+'.json'), 'w', encoding='utf-8') as f: 
            json.dump({'link':link, 'text':scraped_text}, f, ensure_ascii=False)