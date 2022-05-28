from questionmodel import Question
from quizcontroller import QuizController
from ui import QuizInterface
from urllib import request

response = request.get('https://opentdb.com/api.php?amount=100&type=boolean')
question_data  = response.json()["results"]

questions = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quiz = QuizController(questions)
quiz_ui = QuizInterface(quiz)