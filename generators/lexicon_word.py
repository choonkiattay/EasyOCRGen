import json
import random


class LexiconWords(object):

    def __init__(self, number):
        with open ('generators/words_dictionary.json') as json_file:
            self.word_dict = json.load(json_file)
            self.number = number

    def generate_words(self, ):
        max_dict_len = len(list(self.word_dict))
        lex_words = []
        for i in range(self.number):
            lex_word = list(self.word_dict)[random.randint(0, max_dict_len)]
            lex_words.append(lex_word)
        return lex_words
