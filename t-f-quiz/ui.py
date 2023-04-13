from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.q_text = self.canvas.create_text(150, 125, text=f"Question", font=("Arial", 20, "italic"),
                                              fill=THEME_COLOR, anchor="center", width=290)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=text)
        else:
            if self.quiz.score == 10:
                self.canvas.itemconfig(self.q_text, text=f"Good Job! Score: {self.quiz.score}/10")
            elif 10 > self.quiz.score >= 7:
                self.canvas.itemconfig(self.q_text, text=f"You did it! Score: {self.quiz.score}/10")
            elif 7 > self.quiz.score >= 5:
                self.canvas.itemconfig(self.q_text, text=f"You can do better. Score: {self.quiz.score}/10")
            elif self.quiz.score > 5:
                self.canvas.itemconfig(self.q_text, text=f"Try again next time. Score: {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.feedback(self.quiz.check_answer("True"))
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def is_false(self):
        self.feedback(self.quiz.check_answer("False"))
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
