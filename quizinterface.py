from tkinter import *
from quizcontroller import QuizController
from servocontroller import ServoController
import base64

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 28, "italic")

class QuizInterface:
    """
      Sets up UI objects, serves as main driver to call controller methods.
      This is specifically made for a small 800x480 touch-screen display.
    """

    def __init__(self, quiz_controller, servo_controller):
        self.quiz = quiz_controller
        self.servo = servo_controller

        self.initializeCanvas()
        self.get_next_question()

        self.window.mainloop()

    def initializeCanvas(self):
        self.window = Tk()
        self.window.title("Snack Time!")
        self.window.config(bg=THEME_COLOR)
        self.window.geometry("800x480")
        self.window.resizable(False, False)

        self.question_window = Canvas(width=760, height=400, highlightthickness=0)
        self.question_window.grid(column=1, row=2, columnspan=2, padx=20, pady=25)
        self.question_text = self.question_window.create_text(375, 125, font=QUESTION_FONT, text="Question Initialization Error!", fill=THEME_COLOR, width=600)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.place(x=500, y=300)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.place(x=200, y=300)

    def get_next_question(self):
        self.question_window.config(bg="white")
        q_text = self.quiz.next_question()
        if q_text:
            q_text_base64_bytes = q_text.encode("ascii")
            q_text_bytes = base64.b64decode(q_text_base64_bytes)
            try:
                q_text_decoded = q_text_bytes.decode("ascii")
            except UnicodeDecodeError:
                self.get_next_question()
            self.question_window.itemconfig(self.question_text, text=q_text_decoded)
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
            # Open up dialogue in a toplevel window
            top_window = Toplevel(self.window)
            top_window.geometry("800x480")
            top_window.resizable(False, False)
            # This is the button which is used to destroy/close the Toplevel window
            done_button = Button(top_window, text="I am done.", command=top_window.destroy, width=20, bg="red", fg="white", font=("ariel", 24, " bold"))
            Label(top_window, text="The lid is unlocked for snack access! \n\nPlease select the 'I am done.' button\nafter you've grabbed your snack and closed the lid.", font= ('Aerial 20')).pack(pady=50)
            done_button.place(x=175, y=250)
            self.window.wait_window(top_window)
            self.servo.close()
        else:
            self.question_window.config(bg="red")
        self.question_window.after(1000, self.get_next_question)
    