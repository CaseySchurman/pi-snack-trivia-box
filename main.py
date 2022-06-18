from questionmodel import Question
from quizcontroller import QuizController
from servocontroller import ServoController
from ui import QuizInterface

quiz = QuizController()
servo = ServoController()
quiz_ui = QuizInterface(quiz, servo)