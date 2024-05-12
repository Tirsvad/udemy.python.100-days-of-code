import os
import json
import tkinter as tk
import pandas
from random import choice
import constants
from model_settings import SettingsModel, LanguagesAvailableModel


class FlashCard(tk.Tk):
    canvas: tk.Canvas
    menubar: tk.Menu
    window_ask_language: tk.Toplevel

    card_image: int
    card_title: int
    card_word: int

    card_front_img: tk.PhotoImage
    card_back_img: tk.PhotoImage
    button_right_img: tk.PhotoImage
    button_wrong_img: tk.PhotoImage

    languages_available: LanguagesAvailableModel
    # language_to_learn: tuple
    # settings: dict[str: str]
    settings: SettingsModel
    window_after_id = ""
    word: dict

    def __init__(self):
        super().__init__()
        self.settings = SettingsModel(language_to_learn="")
        self.languages_available = LanguagesAvailableModel()

        self.title("Flash Card learning languages")
        self.config(pady=50, padx=50, bg=constants.BACKGROUND_COLOR)
        self.load_defaults_settings()
        self.setup_ui()

        try:
            self.data = (pandas.read_csv(self.languages_available.get_words_to_learn_file_path(self.settings.language_to_learn))
                         .to_dict(orient='records'))
        except FileNotFoundError:
            self.data = (pandas.read_csv(self.languages_available.get_words_file_path(self.settings.language_to_learn))
                         .to_dict(orient='records'))
        self.config(menu=self.menubar)

        self.next_card()

    def load_defaults_settings(self) -> None:
        if os.path.isfile(constants.FILE_SETTINGS):
            with open(constants.FILE_SETTINGS) as f:
                self.settings.__dict__.update(json.load(f))
        else:
            self.settings.language_to_learn = self.languages_available.languages[0][0]
            self.save_default_settings()

    def save_default_settings(self) -> None:
        with open(constants.FILE_SETTINGS, "w") as f:
            f.write(json.dumps(self.settings.__dict__))

    def setup_ui(self) -> None:
        """
        Creating the UI
        :return:
        """
        # Menubar
        self.menubar = tk.Menu(self)
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Language to learn", command=self.ask_language_to_learn)
        file_menu.add_command(label="Close", command=exit)
        self.menubar.add_cascade(label="File", menu=file_menu)

        # Canvas
        self.canvas = tk.Canvas(width=800, height=526, bg=constants.BACKGROUND_COLOR, highlightthickness=0)
        self.card_front_img = tk.PhotoImage(file=constants.FILE_CARD_FRONT_IMAGE)
        self.card_back_img = tk.PhotoImage(file=constants.FILE_CARD_BACK_IMAGE)
        self.card_image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="word", font=("Ariel", 68, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Buttons
        self.button_right_img = tk.PhotoImage(file=constants.FILE_BUTTON_RIGHT_IMAGE)
        button_right = tk.Button(self, image=self.button_right_img, highlightthickness=0, command=self.remove_card)
        button_right.grid(row=1, column=1)

        self.button_wrong_img = tk.PhotoImage(file=constants.FILE_BUTTON_WRONG_IMAGE)
        button_wrong = tk.Button(self, image=self.button_wrong_img, highlightthickness=0, command=self.next_card)
        button_wrong.grid(row=1, column=0)

    def ask_language_to_learn(self) -> None:
        self.window_ask_language = tk.Toplevel(self, padx=50, pady=50)
        self.window_ask_language.title("What languages are we learning")
        self.window_ask_language.transient(self)
        self.window_ask_language.grab_set()
        # self.wait_window(self.window_ask_language)
        window_frame = tk.Frame(self.window_ask_language)
        lb = tk.Listbox(
            window_frame,
        )
        [lb.insert(tk.END, lang[1]) for lang in self.languages_available.languages]

        lb.pack()

        button = tk.Button(
            window_frame,
            text="Choose",
            command=lambda: self.ask_language_to_learn_button_action(lb.curselection())
        )
        button.pack()
        window_frame.pack()

    def ask_language_to_learn_button_action(self, index: tuple) -> None:
        if len(index) == 0:
            print("You didn't choose a language")
        else:
            self.settings.language_to_learn = self.languages_available.languages[index[0]][0]
            print("Changed language to {self.settings.language_to_learn}")
            self.window_ask_language.destroy()
            self.next_card()

    def remove_card(self) -> None:
        """
        Remove the card from deck
        :return:
        """
        self.data.remove(self.word)
        new_data = pandas.DataFrame(self.data)
        new_data.to_csv(
            self.languages_available.get_words_to_learn_file_path(self.settings.language_to_learn),
            index=False)
        self.next_card()

    def next_card(self) -> None:
        """
        Show next card in deck
        :return:
        """
        if self.window_after_id:
            self.after_cancel(self.window_after_id)
        self.word = choice(self.data)
        self.canvas.itemconfig(self.card_image, image=self.card_front_img)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.word["French"], fill="black")
        self.window_after_id = self.after(ms=3000, func=self.show_back_card)

    def show_back_card(self) -> None:
        """
        Showing the translation
        :return:
        """
        self.canvas.itemconfig(self.card_image, image=self.card_back_img)
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.word["English"], fill="white")
