from bs4 import BeautifulSoup
import requests
import os
import json
import pickle

# def ignore_english(text):
#     """
#     Function takes in multi-language text and returns text without the english part in it.
#     """
#     # text = ''.join(i for i in text if ord(i)<65 or (ord(i)<97 and ord(i)> 90) or ord(i)>122)
#     text = " ".join(text.split())
#     return text

def para_scraper(relevant_content):
    scraped_text_list = []
    for para in relevant_content.find_all('p'):
        scraped_text = para.get_text()
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

        source = requests.get(link, headers=headers).text

        soup = BeautifulSoup(source, "lxml")
        
        relevant_content = soup.body.find('div', id="texttospeak")
        if(relevant_content==None):
            print("Oh no!")
        
        scraped_text = relevant_content.get_text()

        with open(os.path.join('API_SCRAPER', 'vikaspedia_agri_text', 'vk_extracted_file_'+str(counter)+'.json'), 'w', encoding='utf-8') as f: 
            json.dump({'link':link, 'text':scraped_text}, f, ensure_ascii=False)
        
        return 0
    except:
        print("Text couldn't be scraped from link!")
        return 1

counter = 0
with open(os.path.join('API_SCRAPER', 'vikaspedia_agri_links'), 'rb') as fp:
    list_of_agri_links = pickle.load(fp)
for link in list_of_agri_links:
    # scrape_text(counter, link)
    # counter+=1
    print(link)