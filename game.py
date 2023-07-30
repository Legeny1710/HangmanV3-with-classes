
class Game:
    def __init__(self, word):
        self.word = word
        self.display = []
        self.userd_word_list = []
        self.lives = 0
        self.display_word = ""
        self.create_display()


    def create_display(self):
        for i in range(0, len(self.word)):
            self.display.append("_")

    def get_user_guess(self):
        user_guess = input("Enter your guess: ")
        return user_guess

    def check_if_letter_is_in_word(self, user_guess):

        index = 0
        if user_guess in self.word:
            for i in range(0, len(self.word)):
                if self.word[i] == user_guess:
                    index = i

            self.display[index] = user_guess
            print(self.display)

    def check_if_user_guessed_all(self):
        user_guess = self.get_user_guess()
        for i in self.display:
            self.display += i

        if self.display == self.word:
            print("you won!")
            return True
        else:
            return False








