import tkinter as tk
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"


class FlashCard:
    window: tk.Tk
    canvas: tk.Canvas
    word: dict
    window_after_id = ""

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Flash Card learning languages")
        self.window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
        self.card_front_img = ""
        self.canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_front_img = tk.PhotoImage(file='images/card_front.png')
        self.card_back_img = tk.PhotoImage(file='images/card_back.png')
        self.card_image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="word", font=("Ariel", 68, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2)

        button_right_img = tk.PhotoImage(file='images/right.png')
        button_right = tk.Button(image=button_right_img, highlightthickness=0, command=self.remove_card)
        button_right.grid(row=1, column=1)

        button_wrong_img = tk.PhotoImage(file='images/wrong.png')
        button_wrong = tk.Button(image=button_wrong_img, highlightthickness=0, command=self.next_card)
        button_wrong.grid(row=1, column=0)
        data = ""
        try:
            data = pandas.read_csv('data/words_to_learn.csv')
        except FileNotFoundError:
            data = pandas.read_csv('data/french_words.csv')
            self.data = data.to_dict(orient='records')
        else:
            # self.data = pandas.DataFrame.to_dict(data, orient='records')
            self.data = data.to_dict(orient='records')

        self.next_card()

        self.window.mainloop()

    def remove_card(self):
        self.data.remove(self.word)
        new_data = pandas.DataFrame(self.data)
        new_data.to_csv("data/words_to_learn.csv", index=False)
        self.next_card()

    def next_card(self):
        if self.window_after_id:
            self.window.after_cancel(self.window_after_id)
        self.word = choice(self.data)
        self.canvas.itemconfig(self.card_image, image=self.card_front_img)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.word["French"], fill="black")
        self.window_after_id = self.window.after(ms=3000, func=self.show_back_card)

    def show_back_card(self):
        self.canvas.itemconfig(self.card_image, image=self.card_back_img)
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.word["English"], fill="white")


App = FlashCard()
