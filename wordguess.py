import random

words = ['bright', 'champs', 'coding', 'github', 'python', 'programming'] # a list of the game's answers

word = random.choice(words)

name = input('Please enter your name : ') # Player's name input section
guessletters = ''
chance = 10 # The amount of wrong guesses that is possible
print("Okay! Let's start guessing") 

while chance > 0: # The main code algorithm
    guess = input("Guess a letter of the word : ") # the letter input
    guessletters += guess # storing all the letters from the input
    wrong = 0 # indicates that there is no mistake
    
    # checking letter one by one using loop
    for letter in word:
        if letter in guessletters:
            print(letter)
        else:
            print('_')
            wrong = 1 # indicates that the letter is wrong

    if wrong ==0: # if the player answer without any mistakes
        print("Congratulations!", name, "you guess all the letters exactly")
        print("the word is : ", word)
        break
    else: # if the player made some mistakes 
        print("Congratulations!", name, "you guess all the letters")
        print("the word is : ", word)
        break

    # punishing the player's mistakes
    if guess not in word: 
        chance -= 1 # reducing the chance of the player to gess the letter
        print("wrong guess, the letter is not in the word")
        print(f"you have {chance} more guess chances")
        if chance == 0: # The game is over if the player losses all the chances
            print("Sorry, your number of chances are over. You lose")
        else: # Player can try again when they still have the chances
            print("You may try again") 