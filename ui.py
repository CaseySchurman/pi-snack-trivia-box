from tkinter import *
from quizcontroller import QuizController
from servocontroller import ServoController
import time

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
  def __init__(self, quizcontroller: QuizController):
    self.quiz = QuizController
    self.servo = ServoController

    self.window = Tk()
    self.window.title("Snack Time!")
    self.window.config(bg=THEME_COLOR)

    # self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="#fff")
    # self.score_label.grid(column=1, row=0, pady=20)

    self.question_window = Canvas(width=300, height=250, highlightthickness=0)
    self.question_window.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

    self.question_text = self.question_window.create_text(150, 125, font=QUESTION_FONT, text="", fill=THEME_COLOR, width=280)

    true_image = PhotoImage(file="images/true.png")
    false_image = PhotoImage(file="images/false.png")
    self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
    self.true_button.grid(column=0, row=2, pady=20)
    self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
    self.false_button.grid(column=1, row=2, pady=20)

    self.get_next_question()

    self.window.mainloop()

  def get_next_question(self):
    self.question_window.config(bg="white")
    q_text = self.quiz.next_question()
    if q_text: 
      self.question_window.itemconfig(self.question_text, text=q_text)
    else: 
      self.quiz.get_questions()
      self.get_next_question()

  def answer_true(self):
    answered_correctly = self.quiz.check_answer("True")
    self.display_choice_feedback(answered_correctly)

  def answer_false(self):
    answered_correctly = self.quiz.check_answer("False")
    self.display_choice_feedback(answered_correctly)

  def display_choice_feedback(self, is_correct):
    if is_correct:
      self.question_window.config(bg="green")
      self.servo.open()
      self.window.after(60000)
      self.servo.close()
    else:
      self.question_window.config(bg="red")
    self.window.after(1000, self.get_next_question)