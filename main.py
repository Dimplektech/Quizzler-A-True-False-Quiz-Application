"""
The main entry point for the quiz application.

This module initializes the quiz, fetches questions, and starts the GUI for the quiz game.

Functions
---------
main():
    Initializes the QuizBrain object and starts the QuizInterface (GUI).
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


