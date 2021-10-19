import json
import os
import re
import csv

with open(os.path.join('agriculture_domain_text_files', 'extracted_file_3.json'), 'r', encoding='utf-8') as fp:
    data = json.load(fp)
    link = data["link"]
    scraped_text = data["text"]

list_of_words_in_file = re.findall(r'[\u0900-\u0d7F\w]+', scraped_text)
# with open('testing_stats.json', 'w', encoding='utf-8') as f: 
#     json.dump({'list of words':list_of_words_in_file}, f, ensure_ascii=False)
# print(list_of_words_in_file)
# num_of_words_in_file = len(list_of_words_in_file)
# print(num_of_words_in_file)
# global_number_of_words += num_of_words_in_file

# ##Make list of sentences in file
split_up_sentences = list(filter(None, re.split("[.|।][^.]", scraped_text)))
# # print(split_up_sentences)
with open('testing_stats.json', 'w', encoding='utf-8') as f: 
    json.dump({'split up sentences':split_up_sentences}, f, ensure_ascii=False)


num_of_sentences_in_file = len(split_up_sentences)
# global_number_of_sentences+= num_of_sentences_in_file
# print(num_of_sentences_in_file)
list_of_words_in_file.sort()

# local_dictionary_of_hindi_words= {}
# prev_word = None    
# for each_word in list_of_words_in_file:
#     if(each_word != prev_word):
#         count = 1
#         local_dictionary_of_hindi_words.update({each_word : count})
#     if(each_word == prev_word):
#         count += 1
#         local_dictionary_of_hindi_words.update({each_word : count})
#     prev_word = each_word

# global_dictionary_of_hindi_words.update(local_dictionary_of_hindi_words)
# with open('testing_stats.json', 'w', encoding='utf-8') as f: 
#     json.dump(local_dictionary_of_hindi_words, f, ensure_ascii=False)