import random

class ChooseWord:
    def __init__(self, word_list):
        self.word_list = word_list
        self.chosen_word = ""

    def generate_random_word(self):
        self.chosen_word = random.choice(self.word_list)
        return self.chosen_word
