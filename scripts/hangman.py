# Import
import re
import random
from art import *
from words import *

# Classe
class Hangman():

    #Constructor Method
    def __init__(self):
        random.shuffle(words)
        self.chosen_word = random.choice(words)
        self.original_chosen_word = self.chosen_word
        self.points = 6
        self.game_is_running = True
        self.reveal_word = ""

        #print(f"[DEBUG] - Selected word by the system was: {self.chosen_word}")
        
    #Method to hide the letter on the board
    def __hide_word(self, word):
        self.hidden_word = ""
        for char in word:
            if char.isalpha():
                self.hidden_word += "_"
            elif char.isspace():
                self.hidden_word += "*"

        return self.hidden_word
    
    #Method to revial the letters that player guess
    def __reveal_letters(self, hidden_word, chosen_word, letter_revial):
        self.hidden_word = list(hidden_word)
        self.indexes = [index for index, char in enumerate(chosen_word) if char == letter_revial]

        for index in self.indexes:
            self.hidden_word[index] = letter_revial

        self.reveal_word = "".join(self.hidden_word)
        return self.reveal_word
        
    #Method to get player input
    def __input_letter(self) -> str:
        self.inputed_letter = str(input("Please, type a letter: "))
        return self.inputed_letter 


    #Method to guess the letter
    def __guess_letter(self, inputed_letter):

        self.inputed_letter = inputed_letter
        
        #print(f"[DEBUG] - Selected letter by the user: {inputed_letter}")

        if inputed_letter in self.chosen_word:
            print("Nice! you are right! 🎉")

            # Revials in the board the letters
            reveal_word = self.__reveal_letters(self.hidden_word, self.original_chosen_word, self.inputed_letter)
            print(f"{reveal_word} \n")

            # Removes from chosen word the letter what player got right.
            self.chosen_word = self.chosen_word.replace(inputed_letter, "") 

        else:
            print("Sorry, you made an mistake in that attempt.")
            self.points -= 1

        return self.points


    def start_game(self):
        print(text2art("Hang Game"))
        print("Starting game! Good luck!")
        self.hidden_word = self.__hide_word(self.chosen_word)
        
        
        print(board[0])
        print(f"Try to guess the word: {self.hidden_word}")

        while self.game_is_running:
            #print(f"[DEBUG] - Quantidade de pontos: {self.points}")


            self.inputed_letter_is_valid = False
            while self.inputed_letter_is_valid == False:
                self.inputed_letter = self.__input_letter()
                self.inputed_letter_is_valid = True if self.inputed_letter.isalpha() == True else False
                print(f"The input {self.inputed_letter} is not a valid letter, try again.") if self.inputed_letter_is_valid == False else None


            self.points = self.__guess_letter(self.inputed_letter)

            print(board[6 - self.points])

            if self.points == 0:
                print("You lose! :(")
                self.game_is_running = False
                print(f"The word was: {self.original_chosen_word}")
            elif self.chosen_word == "":
                print("Congratulations! You won! 🎉")
                self.game_is_running = False
    


