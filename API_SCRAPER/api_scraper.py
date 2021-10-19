import requests
import os
import json
import pickle

response = requests.get("http://data.vikaspedia.in/api/getpages?ln=hi")
print(response.status_code)
content_of_api = json.loads(response.text)
print(type(content_of_api))
list_of_links = []
for page_dict in content_of_api["pagelinks"]:
    link = page_dict["url"]
    if(link!=None):
        check_link = link.split('/')[3]
        if(check_link =="health"):
            list_of_links.append(link)
print(f"length of list of links: {len(list_of_links)}")
# print(list_of_links)
with open(os.path.join('API_SCRAPER', 'vikaspedia_health_links'), 'wb') as fp:
    pickle.dump(list_of_links, fp)
# with open(os.path.join('API_SCRAPER', 'vikaspedia_links'), 'w') as fp:
#     json.dump(, fp)