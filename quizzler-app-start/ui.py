from tkinter import *
import os
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzlerUI:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quizz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="#fff")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background="#fff")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Questions will be there", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, columnspan=2, pady=50)

        img_file_name = "true.png"
        path = os.path.join("images", img_file_name)
        self.right_image = PhotoImage(file=path)
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.checkerTrue)
        self.right_button.grid(row=2, column=0, padx=20, pady=20)
        
        img_file_name = "false.png"
        path = os.path.join("images", img_file_name)
        self.wrong_image = PhotoImage(file=path)
        self.false_button = Button(image=self.wrong_image, highlightthickness=0, command=self.checkerFalse)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if not self.quizz.still_has_questions():
            self.gameOver()
        else:
            self.quizz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.quizz.current_question.text)
        self.canvas.config(bg='white')

    def checkerTrue(self):
        self.giveFeedBack(self.quizz.check_answer("true"))
        self.score_label.config(text=f"Score: {self.quizz.score}")

    def checkerFalse(self):
        self.giveFeedBack(self.quizz.check_answer("false"))
        self.score_label.config(text=f"Score: {self.quizz.score}")

    def giveFeedBack(self, result: bool):
        if self.quizz.still_has_questions():
            if result:
                self.canvas.config(bg='green')
            else:
                self.canvas.config(bg='red')
            self.canvas.after(300, self.get_next_question)

    def gameOver(self):
        self.canvas.itemconfig(self.question_text, text=f"{self.quizz.score}/10")
