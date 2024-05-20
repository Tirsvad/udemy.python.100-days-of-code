import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')
CANVAS_BG = "white"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.configure(pady=20, padx=20, bg=THEME_COLOR)
        self.window.title("Quizzler")

        self.score_label = tk.Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(self.window, bg=CANVAS_BG, width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="question",
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file="images/true.png")
        false_image = tk.PhotoImage(file="images/false.png")

        self.button_true = tk.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.button_false = tk.Button(image=false_image, highlightthickness=0, command=self.false_pressed)

        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)


        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.configure(bg=CANVAS_BG)
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="We have no more question.")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")

    def true_pressed(self):
        self.answer_feed_back(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.answer_feed_back(self.quiz.check_answer("false"))

    def answer_feed_back(self, status):
        if status:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.score_label.configure(text=f"Score: {self.quiz.score}")
        self.window.after(1000, func=self.get_next_question)
