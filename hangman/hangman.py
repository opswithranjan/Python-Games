import random
from os import path
import hangman_words
from hangman_art import logo
from hangman_art import stages
chosen_word=random.choice(hangman_words.word_list)
print(f'the chosen word is : {chosen_word}\n')
display=[]
print(logo)
for i in range(len(chosen_word)):
    display += "_"
print(display)
lives=6
while True:
    guess=input("please guess a letter: ").lower()
    if guess in display:
        print("you already guessed this word")
    for i in range(len(chosen_word)):   
        if chosen_word[i]==guess:
            display[i]=guess
    if guess not in chosen_word:
        lives -= 1
        print(f'remaining lives: {lives}')
        if lives==0:
            print("You Lost NIGGA")
            print(stages[lives])
            break
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("You Won")
        break
    print(stages[lives])
