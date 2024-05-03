from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"

class Pomodoro:
    def __init__(self):
        self.reps = 0
        self.timer = None
        self.check_marks = ""

        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)

        self.tomato_img = PhotoImage(file="tomato.png")

        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.canvas_timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(row=1, column=1)

        self.headline_label = Label(text="Timer", font=(FONT_NAME, 46, "normal"), bg=YELLOW, fg=GREEN)
        self.headline_label.grid(row=0, column=1, pady=10)

        self.start_button = Button(text="Start", command=self.start_timer, highlightthickness=0)
        self.start_button.grid(row=2, column=0, pady=10)

        self.reset_button = Button(text="Reset", command=self.reset, highlightthickness=0)
        self.reset_button.grid(row=2, column=2, pady=10)

        self.status_mark_label = Label(bg=YELLOW, fg=GREEN)
        self.status_mark_label.grid(row=3, column=1, pady=10)

        self.window.mainloop()

    def reset(self):
        self.reps = 0
        self.check_marks = ""
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.canvas_timer_text, text="00:00")
        self.canvas.itemconfig(self.check_marks, text="")
        self.headline_label.config(text="Timer", fg=GREEN)


    def start_timer(self):
        self.reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.headline_label.config(text="Break", fg=RED)
            self.count_down(long_break_sec)
        elif self.reps % 2 == 0:
            self.headline_label.config(text="Break", fg=PINK)
            self.count_down(short_break_sec)
        else:
            self.headline_label.config(text="Work", fg=GREEN)
            self.count_down(work_sec)

    def count_down(self, count):
        minutes = int(count / 60)
        if minutes < 10:
            minutes = f"0{minutes}"
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"
        self.canvas.itemconfig(self.canvas_timer_text, text=f"{minutes}:{seconds}")
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            if self.reps % 2 == 0:
                self.check_marks += CHECKMARK
                self.status_mark_label.config(text=self.check_marks)


app = Pomodoro()

# ---------------------------- TIMER RESET ------------------------------- #
# ---------------------------- TIMER MECHANISM ------------------------------- #
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# ---------------------------- UI SETUP ------------------------------- #


