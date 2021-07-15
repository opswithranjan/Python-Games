import random
from art import logo
print(logo)
turns=0


def diff():
    diff=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff=='easy':
        return 10
    else:
        return 5

def check(guess,number,turns):
    if guess > number :
        print("Too High!")
        return turns - 1
    elif guess < number :
        print("Too Less!")
        return turns - 1
    else:
        print(f"You got it right.The answer was {number}")
        return 0

def game(): 
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    number=number=random.randint(1,100)
    turns=diff()
    guess=0
    while guess != number:
        print(f"You have {turns} attempts left to guess the number.\n")
        guess=int(input("make a guess: "))
        turns=check(guess,number,turns)
        if turns ==0:
            print("You lost all the chances,Game over!\n")
            return
        elif guess != number:
            print("Guess again\n")
game()
