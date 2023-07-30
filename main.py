from data import logo, stages, wordList
from choose_word import ChooseWord
from game import Game

print(logo)

word = ChooseWord(wordList).generate_random_word()



print(word)

Game(word).check_if_letter_is_in_word(Game(word).get_user_guess())



