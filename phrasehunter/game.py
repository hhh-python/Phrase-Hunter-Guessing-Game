import random
from phrasehunter.phrase import Phrase
import sys


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
                        'Luke I am your father',
                        'Hello there',
                        'You fool I have been trained in your Jedi arts by Count Dooku',
                        'Only a sith deals in absolutes',
                        'He is the chosen one you must see it'
                        ]
        self.active_phrase = None
        self.guesses = []

    def welcome(self):
        print('Welcome to the Python version of WHEEL OF FORTUNE!')

    #Start the game and evaluates guesses and updates the hideen phrase
    #Also determines if the user has descovered the phrase or not
    #Lastly checks if user still wants to play another game
    def start(self):
        self.active_phrase = self.get_random_phrase()
        phrase = Phrase(self.active_phrase)
        self.welcome()
        print(''.join(phrase.display()))
        while True:
            try:
                self.get_guess()
                if not self.guesses[-1].isalpha():
                    raise ValueError('Inputted value is not a letter')
                elif len(self.guesses[-1]) > 1:
                    raise ValueError('Please input only 1 letter at a time')
            except ValueError as e:
                print(F'INVALID VALUE: ({e})')
            else:
                phrase.check_letter(self.guesses[-1])
                if self.guesses[-1] in phrase.phrase:
                    print(''.join(phrase.display()))
                else:
                    self.missed += 1
                    print(f'You got {7 - self.missed} out of 7 trys left!')
                    print(''.join(phrase.display()))
                if '_ ' not in phrase.display():
                    self.game_over(True)
                    play = input('Play again? (Type Yes to play again OR type No to the end game): ').lower()
                    if play == 'yes':
                        self.missed = 0
                        self.start()
                    elif play == 'no':
                        sys.exit()
                elif self.missed == 7:
                    self.game_over(False)
                    play = input('Play again? (Type Yes to play again OR type No to the end game): ').lower()
                    if play == 'yes':
                        self.missed = 0
                        self.start()
                    elif play == 'no':
                        sys.exit()
                          
    def get_random_phrase(self):
        return random.choice(self.phrases)  

    def get_guess(self):
        guess = input('Guess a letter!: ')
        self.guesses.append(guess)

    #A boolean value will be set as an argument based on if user has run
    #Out of guesses or discovered the hidden phrase all together 
    def game_over(self, boolean):
        if boolean:
            print('\n', 'Awesome you figured out the hidden phrase!', '\n')
            print('You are on this counsel but we do not grant you the rank of MASTER!', '\n')
        else:
            print('\n', 'Hahaha (Cough) .. (Cough)  YOU LOSE KENOBI !!', '\n')
