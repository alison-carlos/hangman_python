from hangman import *

class Menu():

    def __init__(self) -> None:
        self.score = 0
        self.keep_game_running = True
        self.run_again = None


    #Method to get user input
    def __user_input(self, question) -> str:
        self.user_input = str(input(f"{question}"))
        return self.user_input 


    def run_game(self):
        
        while self.keep_game_running == True:
            hangman = Hangman()
            hangman.start_game()

            while self.run_again not in ("Y", "N"):
                self.run_again = self.__user_input("Want play again? Please Type 'Y' or 'N'. \n").upper()

            # Stop the game if run_again == No    
            if self.run_again.upper() == "N":
                self.keep_game_running = False




