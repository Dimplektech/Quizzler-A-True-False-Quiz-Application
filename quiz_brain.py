import html
class QuizBrain:
    """
        A class to represent the logic and functionality of the quiz.

        Attributes
        ----------
        question_list : list
            A list of Question objects used in the quiz.
        question_number : int
            Tracks the current question number.
        score : int
            Keeps track of the user's score.

        Methods
        -------
        still_has_questions():
            Checks if there are any remaining questions.
        next_question():
            Retrieves the next question and formats it for display.
        check_answer(user_answer):
            Compares the user's answer to the correct answer and updates the score.
        """

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text =html.escape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:

            return False


