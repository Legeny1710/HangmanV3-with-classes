
class Game:
    def __init__(self, word, stages):
        self.word = word
        self.display = []
        self.used_word_list = []
        self.lives = 7
        self.display_word = ""
        self.create_display()
        self.stages_num = 6
        self.is_game_on = False
        self.stages = stages


    def create_display(self):
        for i in range(0, len(self.word)):
            self.display.append("_")

    def get_user_guess(self):
        user_guess = input("Enter your guess: ")
        return user_guess

    def print_information(self):
        print(self.display)
        print(f'Used Word List: {self.used_word_list}')
        print(f'Lives: {self.lives}')

    def check_answer(self, user_guess):
        for i in range(0, len(self.word)):
            if self.word[i] == user_guess:
                self.display[i] = user_guess
                self.is_game_on = True

        if user_guess not in self.word:
            print("Oops, Try Again!")
            print(self.stages[self.stages_num])
            self.stages_num -= 1

        if self.lives == 0:
            print("You ran out of guesses! You Lost!")


        if user_guess in self.used_word_list:
            print("You already have guessed this letter! Try Again!")
        else:
            self.lives -= 1
            self.used_word_list.append(user_guess)

        self.displayWord = ""
        for i in self.display:
            self.displayWord += i

        if self.word == self.displayWord:
            print("You Win!")
            self.is_game_on = False

        if self.word == user_guess:
            print("Nice guess, You win!")
            self.is_game_on = False

    def play(self):
        self.is_game_on = True
        while self.is_game_on == True and self.lives != 0:
            self.print_information()
            self.check_answer(self.get_user_guess())
        else:
            print("You Lost!")











