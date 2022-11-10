#!/usr/bin/env python3

""" Requirements:
# Return unique answers based on the input provided... multiple results should be possible.
# AS BEST YOU'RE ABLE, control for user errors (suggested: methods, try/except, while loop)
# Use at least one while loop.
# ROUGH minimum of 40 lines of code... if code is spread out across multiple files, they are cumulative."""

from question_model import Question
from data import questions
from quiz_engine import QuizEngine

# make question list
question_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)

# init quiz with question_bank
quiz = QuizEngine(question_bank)

# check if quiz still has more questions remaining
while quiz.questions_remaining():
    quiz.next_question()

final_success_rate = int(quiz.score / quiz.question_number * 100)

print("We've reached the end of the road -- Congrats, you've completed the quiz!")
print(f"Your final score is: {quiz.score} / {quiz.question_number}.")
print(f"That's a final success rate of {final_success_rate}%.")
