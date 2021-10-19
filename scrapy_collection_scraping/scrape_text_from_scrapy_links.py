import json
import scrape_text
import os

with open('netinbag_finance_hindi_links.json', 'r') as fp:
    data = json.load(fp)
links = []
for item in data:
    links.append(item["Link"])


# with open('exceptionlinks_VIKASPEDIA_AGRI.txt', 'r') as fp:
#     links_for_selenium = (fp.read()).split('\n')
#     del links_for_selenium[-1]
# print(links_for_selenium)
# print(len(links_for_selenium))

link_exceptions = []
i = 0
for link in links:
    # print(link)
    flag = scrape_text.scrape_text(i, link)
    if(flag):
        link_exceptions.append(link)    
    i+=1

with open(os.path.join('exceptionlinks_NETINBAG_FIN_HINDI.txt'), 'a') as f:
    for exceptionlink in link_exceptions:
        f.write(exceptionlink)
        f.write('\n')

print("finished! :)")