class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.hidden_phrase = []
    
    #Determines if phrase is already transformed into a hidden phrase
    #By checking if the hidden phrase list is empty
    #And if it is not empty it will return an updated phrase based off
    #The the check_letter() method
    def display(self):
        if not len(self.hidden_phrase):
            for value in self.phrase:
                if value.isalpha():
                    self.hidden_phrase.append('_ ')
                else:
                    self.hidden_phrase.append(' ')
            return self.hidden_phrase
        else:
             return self.hidden_phrase

    #Evaluates each letter in the phrase to determine if they match
    #The current guessed letter and if it is a match 
    #The method will target the specific index the letter is at in the self.phrase
    #And update the same index in hidden phrase list to the value of the current guess
    def check_letter(self, guess):
        for index, value in enumerate(list(self.phrase)):
            if guess.lower() == value:
                self.hidden_phrase[index] = guess.lower()
