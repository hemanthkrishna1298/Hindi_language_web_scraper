import os
import json
import pickle
import shutil

with open ('agriculture_list_of_links', 'rb') as fp:
    list_of_agri_links = pickle.load(fp)
with open ('finance_list_of_links', 'rb') as fp:
    list_of_fin_links= pickle.load(fp)
with open ('general_list_of_links', 'rb') as fp:
    list_of_gen_links= pickle.load(fp)


for filename in os.listdir('savetext'):
    with open(os.path.join('savetext', filename), 'r', encoding='utf-8') as fp:
        data = json.load(fp)
        linkname = data["link"]
        if (linkname in list_of_agri_links):
            shutil.copy(os.path.join('savetext', filename), os.path.join('agriculture_domain_text_files', filename))
        if (linkname in list_of_fin_links):
            shutil.copy(os.path.join('savetext', filename), os.path.join('finance_domain_text_files', filename))
        if (linkname in list_of_gen_links):
            shutil.copy(os.path.join('savetext', filename), os.path.join('general_domain_text_files', filename))