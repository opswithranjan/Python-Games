import random
from art import logo

number=random.randint(1,100)
print(logo)
def game(number):
    game_over=False
    diff=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff=='easy':
        lives=10
    else:
        lives=5
    while not game_over:
        print(f"You have {lives} attempts left to guess the number.\n")
        if lives>0:
            guess=int(input("make a guess: "))
        # result=get_result(guess)
        if lives==0:
            game_over=True
            print("You lost all the chances,Game over!\n")
            break
        elif number > guess and lives > 0:
            print("Too low\nguess again\n")
            lives -= 1
        elif number < guess and lives > 0 :
            print("Too high\nguess again\n")
            lives -= 1
        elif number==guess and lives > 0 :
            game_over=True
            print("You Won\n")
            break
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
game(number)