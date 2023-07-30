from data import logo, stages, wordList
from choose_word import ChooseWord
from game import Game

print(logo)

word = ChooseWord(wordList).generate_random_word()
print(word)

Game(word, stages).play()



