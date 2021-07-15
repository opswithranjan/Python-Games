import random
import os
from art import logo
from art import vs
from game_data import data

def compare(cand1,cand2):
    print(f"Compare A: {cand1.get('name')}, a {cand1.get('description')}, from {cand1.get('country')},{cand1.get('follower_count')}")
    print(vs)
    print(f"Compare B: {cand2.get('name')}, a {cand2.get('description')}, from {cand2.get('country')},{cand2.get('follower_count')}")

def game():
    cand1=random.choice(data)
    cand2=random.choice(data)
    game_over=False
    score = 0
    while not game_over:
        os.system('clear')
        print(logo)
        if cand1==cand2:
            cand2=random.choice(data)
        compare(cand1,cand2)
        count1=cand1.get('follower_count')
        count2=cand2.get('follower_count')
        choice=input("Who has more followers? Type 'A' or 'B': ").upper()
        if choice == 'A':
            if count1 > count2 :
                cand2=random.choice(data)
                score += 1
                print(f"You are right.Current score: {score}")
            elif count2 > count1:
                print(f"Sorry,that's wrong. Final score: {score}")
                game_over=True
        elif choice == 'B':
            if count2 > count1 :
                cand1=cand2
                cand2=random.choice(data)
                score += 1
                print(f"You are right.Current score: {score}")
            elif count1 > count2:
                print(f"Sorry,that's wrong. Final score: {score}")
                game_over=True  
        else:
            print("Invalid input.Please Try again!")
            game_over=True             

game()

