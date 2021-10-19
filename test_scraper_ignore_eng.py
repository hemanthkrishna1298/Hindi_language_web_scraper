from bs4 import BeautifulSoup
import requests
import os
import json
import re
import ssl

gcontext = ssl.SSLContext()
# use header if access is denied.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
# agent = {"User-Agent":"Mozilla/5.0"}

def ignore_english(text):
    """
    Function takes in multi-language text and returns text without the english part in it.
    """
    text = ''.join(i for i in text if ord(i)<65 or (ord(i)<97 and ord(i)> 90) or ord(i)>122)
    text = " ".join(text.split())
    return text

link = "https://hi.quora.com/%E0%A4%8F%E0%A4%A8%E0%A4%AA%E0%A5%80%E0%A4%95%E0%A5%87-%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE-%E0%A4%B9%E0%A5%88-%E0%A4%87%E0%A4%B8%E0%A4%95%E0%A4%BE-%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A4%BE-%E0%A4%A8%E0%A4%BE%E0%A4%AE"
source = requests.get(link, headers = headers).text

soup = BeautifulSoup(source, "lxml")
# print(soup.prettify)
#scraped_text_list = []
# relevant_content = (((soup.body.find('tr')).find_all('tr'))[2]).find_all('tr')[2]
# print(relevant_content_1.prettify)
# relevant_content = soup.body.find('section', class_="article-detail auw-lazy-load")
# relevant_content2 = relevant_content.find_all('div', class_= "CssComponent-sc-1oskqb9-0 cXjXFI")
relevant_content = soup.body.find('article', id="fullArticle")
# if(relevant_content==None):
    # relevant_content = soup.body.find('section', class_="lead-gallery auw-lazy-load")
#for para in relevant_content:
scraped_text = relevant_content.get_text()

# if(len(text)>0):
#     scraped_text_list.append(text)
# scraped_text = ""
# scraped_text = scraped_text.join(scraped_text_list)
with open(os.path.join('hello'+'.json'), 'w', encoding='utf-8') as f: 
            json.dump({'link':link, 'text':scraped_text}, f, ensure_ascii=False)