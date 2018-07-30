# -*- coding: utf-8 -*-

import json
# import xml.etree.ElementTree as ET
# import re
import os

file_format = 'json'
# file_format = 'xml'

file_list = os.listdir(os.path.dirname(os.path.abspath(__file__)))

# words_rating = dict()

for file_name in file_list:
    if file_name[len(file_name) - len(file_format):len(file_name)] == file_format:
        print(file_name, '\n')
        with open(file_name, encoding='utf-8', mode='r') as input_file:
            file_data = json.load(input_file)
            news_list = file_data['rss']['channel']['items']
            news_word_list = []
            words_rating = dict()
            for news in news_list:
                news_line = news['description']
                news_word_list = news_line.split(' ')

                for word in news_word_list:
                    if len(word) > 6:
                        if word not in words_rating.keys():
                            words_rating[word] = 1
                            # print('!!!')
                        else:
                            words_rating[word] += 1
                            # print('&')

            news_word_sorted_list = sorted(news_word_list)
            print(news_word_sorted_list)
            print(words_rating)
            for word in words_rating.keys():
                if words_rating[word] > 13:
                    print('Key: {} Val: {}'.format(word, words_rating[word]))
