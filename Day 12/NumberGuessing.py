import random
import os

def trick(number, num, lives):
    if number > num:
        print("Too high.\nGuess again.")
        return lives-1
    elif number < num:
        print("Too low.\nGuess again.")
        return lives-1
    else:
        print(f"You won, the number was {num}. :D ")
        return -1

def program():
    os.system('clear')
    num = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    
    while True:
        
        if lives==0:
            print("You've run out of guesses, you lose.")
            break
        numGuess = int(input("Make a guess: "))
        
        lives = trick(numGuess, num, lives)
        if lives==-1:
            break
        print(f"You have {lives} attempts remaining to guess the number")
        
program()
        