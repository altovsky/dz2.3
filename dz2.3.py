# -*- coding: utf-8 -*-

import json
# import xml.etree.ElementTree as ET
import os

file_format = 'json'
# file_format = 'xml'
min_number_of_letters = 6
rate_threshold = 10


def read_file_content(file_name_value, encoding_type):
    with open(file_name_value, encoding=encoding_type, mode='r') as input_file:
        return json.load(input_file)


def extract_counted_news(file_data):
    news_list = file_data['rss']['channel']['items']
    words_rated_dict = dict()
    for news in news_list:
        news_line = news['description']
        news_word_list = news_line.split(' ')

        for word_val in news_word_list:
            if len(word_val) > min_number_of_letters:
                if word_val not in words_rated_dict.keys():
                    words_rated_dict[word_val] = 1
                else:
                    words_rated_dict[word_val] += 1
    return words_rated_dict


def find_all_values(word_val, word_dictionary):
    rate_val = word_dictionary[word_val]
    word_list = []
    for word_in_dict in word_dictionary:
        if word_dictionary[word_in_dict] == rate_val and word_in_dict not in word_list:
            word_list.append(word_in_dict)
    return word_list


file_list = os.listdir(os.path.dirname(os.path.abspath(__file__)))

print('Tоп {} самых часто встречающихся в '
      'новостях слов длиннее {} символов.\n'.format(rate_threshold, min_number_of_letters))
for file_name in file_list:
    if file_name[len(file_name) - len(file_format):len(file_name)] == file_format:
        file_content = read_file_content(file_name, 'utf-8')
        news_dict = extract_counted_news(file_content)
        words_sorted = sorted(news_dict, key=lambda x: news_dict[x], reverse=True)
        words_rated_sorted = words_sorted[0:rate_threshold]
        print('В файле {}: '.format(file_name))
        for word in words_rated_sorted:
            print('{} - {}'.format(word, news_dict[word]))
        print('')
