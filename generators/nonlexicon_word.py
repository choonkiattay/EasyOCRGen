import numpy as np
import os


class NonlexiconWord(object):

    def __init__(self, number):
        # print("Non Lexicon Words")
        self.number = number
        self.words_list = []
        self.dict = [class_name.rstrip('\n') for class_name in open('generators/dictionary')]

    def generate_words(self, word_length=10):

        for i in range(self.number):
            char = str(self.dict[np.random.randint(0, 58)])
            for j in range(word_length):
                char += str(self.dict[np.random.randint(0, 58)])
            self.words_list.append(char)
        return self.words_list
