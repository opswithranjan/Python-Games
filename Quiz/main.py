import random
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from art import logo
from os import system

system("clear")
print(logo + "\n\n")
question_bank = []
for each in question_data:
    question = Question(each["text"], each["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    user = quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
