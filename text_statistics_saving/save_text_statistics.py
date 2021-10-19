import json
import os
import re
import csv

global_dictionary_of_hindi_words={}
global_number_of_words = 0
global_number_of_sentences = 0


# count number of unique words, store frequency of each unique word as dict
csv_file1 = open(os.path.join('stats_for_each_file_in_each_domain', 'stats_for_each_file_in_general', "num_words_sentences_in_each_file.csv"), 'w', encoding='utf-8')
csv_writer1 = csv.writer(csv_file1)
csv_writer1.writerow(['Filename', 'Link', 'Number of Words', 'Number of Sentences'])

for filename in os.listdir('general_domain_text_files'):
    with open(os.path.join('general_domain_text_files', filename), 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    link = data["link"]
    scraped_text = data["text"]
    ##Make list of words in file
    list_of_words_in_file = re.findall(r'[\u0900-\u0d7F\w]+', scraped_text)
    # print(list_of_words_in_file)
    num_of_words_in_file = len(list_of_words_in_file)
    global_number_of_words += num_of_words_in_file

    ##Make list of sentences in file
    split_up_sentences = list(filter(None, re.split("[.|।][^.]", scraped_text)))        ## if length of sentence less than 3-4 words, then don't partition
    # print(split_up_sentences)
    num_of_sentences_in_file = len(split_up_sentences)
    global_number_of_sentences+= num_of_sentences_in_file

    list_of_words_in_file.sort()

    # make local frequency count of words as a dict
    local_dictionary_of_hindi_words= {}
    prev_word = None    
    for each_word in list_of_words_in_file:
        if(each_word != prev_word):
            count = 1
            local_dictionary_of_hindi_words.update({each_word : count})
        if(each_word == prev_word):
            count += 1
            local_dictionary_of_hindi_words.update({each_word : count})
        prev_word = each_word
    
    for word, count in local_dictionary_of_hindi_words.items():
        if word in global_dictionary_of_hindi_words:
            global_dictionary_of_hindi_words[word] +=count
        else:
            global_dictionary_of_hindi_words.update({word : count})

    csv_writer1.writerow([filename, link, num_of_words_in_file, num_of_sentences_in_file])

csv_file1.close()

csv_file2 = open(os.path.join('stats_for_each_file_in_each_domain', 'stats_for_each_file_in_general', "total_words_and_sentences_in_gen.csv"), 'w', encoding='utf-8')
csv_writer2 = csv.writer(csv_file2)
csv_writer2.writerow(['Domain name', 'Total words', 'Total sentences'])
csv_writer2.writerow(['General', global_number_of_words, global_number_of_sentences])

csv_file3 = open(os.path.join('stats_for_each_file_in_each_domain', 'stats_for_each_file_in_general', "word_frequencies.csv"), 'w', encoding='utf-8')
csv_writer3 = csv.writer(csv_file3)
csv_writer3.writerow(['Word', 'Frequency'])
for word, frequency in global_dictionary_of_hindi_words.items():
    csv_writer3.writerow([word, frequency])