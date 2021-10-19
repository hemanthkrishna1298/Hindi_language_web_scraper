from bs4 import BeautifulSoup
import requests
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def ignore_english(text):
    """
    Function takes in multi-language text and returns text without the english part in it.
    """
    # text = ''.join(i for i in text if ord(i)<65 or (ord(i)<97 and ord(i)> 90) or ord(i)>122)
    text = " ".join(text.split())
    return text

def para_scraper(relevant_content):
    scraped_text_list = []
    for para in relevant_content.find_all('p'):
        scraped_text = para.get_text()
        scraped_text = ignore_english(scraped_text)
        if(len(scraped_text)>0):
            scraped_text_list.append(scraped_text)
        scraped_text = ""
        scraped_text = scraped_text.join(scraped_text_list)
    return scraped_text

def scrape_text(counter, link):
    """
    This function scrapes text from each link.
    """

    # Modify the below code for each specific website for scraping out the relevant text
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(link)
        time.sleep(3)
        source = driver.page_source
        driver.quit()

        # source = requests.get(link, headers=headers).text
        soup = BeautifulSoup(source, "lxml")
        # print(soup.prettify)
        #scraped_text_list = []
        if(soup.body.find('h3', class_="folder_heading")):
            print("not an article!" + str(counter))
            return 1
        relevant_content = soup.body.find('div', id="texttospeak")
        # if(relevant_content==None):
            # relevant_content = soup.body.find('div', class_="article-para")

        # relevant_content = soup.body.find('article', class_="item-page")

        #     scraped_text = relevant_content.get_text()
        #     if(len(scraped_text)>0):
        #         scraped_text_list.append(scraped_text)
        #     scraped_text = ""s
        #     scraped_text = scraped_text.join(scraped_text_list)
        #     scraped_text = ignore_english(scraped_text)
        
        
        scraped_text = relevant_content.get_text()
        # scraped_text = para_scraper(relevant_content)
            # print(scraped_text)

        with open(os.path.join('vikaspedia_scraped_text_AGRI_BENGALI', 'vp_extracted_file_agri_bn'+str(counter)+'.json'), 'w', encoding='utf-8') as f: 
            json.dump({'link':link, 'text':scraped_text}, f, ensure_ascii=False)

        # with open(os.path.join('savetext', str(link)), 'w', encoding='utf-8') as f:
        #     f.write(scraped_text)
        
        return 0
    except:
        print("Text couldn't be scraped from link! "+str(counter))

        return 1