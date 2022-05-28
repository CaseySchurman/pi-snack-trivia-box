from urllib import request
from questionmodel import Question

class QuizController:
    def __init__(self, q_list):
        self.num = 0
        self.question_list = q_list
        self.current_question = None

    def generate_question(self):
        self.current_question = self.question_list[self.num]
        self.num += 1
        user = input(f'Q.{self.num} {self.current_question.text} ').title()
        #self.check_answer(user, current.answer)

    def next_question(self):
        for _ in self.question_list:
            self.generate_question()
        else:
            return False

    def check_answer(self, answer):
        correct_answer = self.current_question.answer
        if answer == correct_answer:
            print("Correct!\n")
            #self.score += 1
            #print(f"Correct, score = {self.score}/{self.num}.\n")
        else:
            print("Wrong!\n")
            #print(f"Wrong, score = {self.score}/{self.num}.\n")

    def get_questions(self):
        response = request.get('https://opentdb.com/api.php?amount=100&type=boolean')
        question_data  = response.json()["results"]

        questions = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            questions.append(new_question)

        self.question_list = questions
        self.num = 0