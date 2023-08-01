from data import logo, stages, wordList
from choose_word import ChooseWord
from game import Game

print(logo)

word = ChooseWord(wordList).generate_random_word()
print(word)

g = Game(word, stages)

g.is_game_on = True
while g.is_game_on == True and g.lives != 0:
    g.print_information()
    g.check_answer(g.get_user_guess())




