import json
import os
import re

with open('vikaspedia_agri_bengali_links.json', 'r') as fp:
    data = json.load(fp)

new_data = []
for item in data:
    link = item["Link"]
    if bool(re.search(r'\d', link)):
        new_data.append(item)    

with open('vikaspedia_agri_bengali_links_updated.json', 'w') as fp:
    json.dump(new_data, fp)

# print(bool(re.search(r'\d', "https://bn.vikaspedia.in/agriculture/post-harvest-technologies/natural-resins-and-gums-of-commercial-importance/dammar")))