# from random_word import RandomWords


class LexiconWords(object):

    def __init__(self, number):
        self.r = RandomWords()
        self.number = number
        # self.word_list =[]

    def generate_words(self, ):
        # for i in range(number):
        lex_words = self.r.get_random_words(limit=self.number)
        return lex_words
