import requests
import base64
from questionmodel import Question

# We pull in 100 questions at a time
QUESTION_COUNT = 100

class QuizController:
    """
    Handles logic for pulling questions from opentdb and decoding the base64 encoded data, checking answers, and 
    getting the next question when user is playing the trivia game.
    """

    def __init__(self):
        self.num = 0
        self.question_list = []
        self.current_question = None
        self.get_questions()

    def get_question(self):
        self.current_question = self.question_list[self.num]
        self.num += 1
        return self.current_question.text

    def next_question(self):
        if self.num < QUESTION_COUNT:
            for _ in self.question_list:
                return self.get_question()
            else:
                return ""
        else:
            return ""

    def check_answer(self, answer):
        if answer == self.current_question.answer:
            return True
        else:
            return False

    def get_questions(self):
        response = requests.get(f'https://opentdb.com/api.php?amount={QUESTION_COUNT}&type=boolean&encode=base64')
        question_data  = response.json()["results"]

        # Certain Q/A's don't come in as valid base64 to be decoded, so just skip if we run into those
        questions = []
        for question in question_data:
            question_text = question["question"]
            try:
                question_decoded = self.decode_base64(question_text)
            except UnicodeDecodeError:
                continue

            question_answer = question["correct_answer"]
            try:
                correct_answer_decoded = self.decode_base64(question_answer)
            except UnicodeDecodeError:
                continue

            new_question = Question(question_decoded, correct_answer_decoded)
            questions.append(new_question)

        self.question_list = questions
        self.num = 0

    def decode_base64(self, value):
        value_base64_bytes = value.encode("ascii")
        value_bytes = base64.b64decode(value_base64_bytes)
        value_decoded = value_bytes.decode("ascii")
        return value_decoded