from question_model import Question
from typing import Text


class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        while True:
            current_question = self.question_list[self.question_number].text
            current_answer = self.question_list[self.question_number].answer
            self.question_number += 1
            user = input(
                f"Q.{self.question_number}: {current_question}. (True/False) :"
            )
            self.check_answer(user, current_answer)
            return self.question_number

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user, current_answer):
        if user.lower() == current_answer.lower():
            print("You Got it right!")
            self.score += 1
        else:
            print("Uh oh ! Wrong answer")
        print(f"The correct answer was: {current_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n\n")
