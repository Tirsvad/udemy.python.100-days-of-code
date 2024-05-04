# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
import json
import os.path
from tkinter import simpledialog

FONT = ("Courier", 12, "normal")
ELEMENT_PADX = 5
ELEMENT_PADY = 5

COLOR_TEXT = "#874F51"
COLOR_BG = "#90AEAD"
COLOR_ELEMENT_FOCUS = "#D4483B"
COLOR_ELEMENT = "#FBE9D0"


class PasswordManager:
    def __init__(self):
        # file_data: dict
        #     "file_data_version": float,
        #     "username_default" : str
        #     "webpages": list
        #             "webpage": str
        #             "username": str
        #             "password": str
        self.file_data = {
            "file_data_version": 1,
            "webpages": [
            ],
        }
        self.data_file_path = "data.json"
        self.default_username = ""

        self.root = Tk()
        self.root.title("Password Manager")
        self.root.option_add("*Background", COLOR_BG)
        self.root.option_add("*Button.Background", COLOR_ELEMENT_FOCUS)
        self.root.config(padx=50, pady=50, bg=COLOR_BG)

        self.logo_img = PhotoImage(file="logo.png")

        self.menu_frame = None
        self.list_frame = None

        # create frame
        self.add_frame = Frame(self.root)
        # create widgets for add_frame
        self.website_label = Label(self.add_frame, text="Website:", font=FONT)
        self.website_username = Label(self.add_frame, text="Email / user name:", font=FONT)
        self.website_password_label = Label(self.add_frame, text="Password:", font=FONT)
        self.website_entry = Entry(self.add_frame, width=43)
        self.website_username_entry = Entry(self.add_frame, width=43)
        self.website_password_entry = Entry(self.add_frame, width=23)

        self.generate_password_button = Button(self.add_frame, text="Generate password")
        self.add_button = Button(self.add_frame, text="Add", width=36, command=self.frame_add_button_add_command)

    def ask_for_default_username(self):
        self.file_data["username_default"] = simpledialog.askstring(title="Default username",
                                                    prompt="Your most common username / email?")
        self.file_save()

    def create_menu_frame(self):
        #
        # Frame for adding password
        #
        self.menu_frame = Frame(self.root)

        canvas = Canvas(self.menu_frame, width=200, height=200, highlightthickness=0)
        canvas.create_image(100, 100, image=self.logo_img)
        add_button = Button(self.menu_frame, text="Add new password", command=self.create_frame_add)
        show_button = Button(self.menu_frame, text="Show your passwords", command=self.create_list_frame)
        setting_username_button = Button(self.menu_frame, text="Default username", command=self.ask_for_default_username)

        canvas.grid(row=1, column=0, columnspan=3)
        add_button.grid(row=0, column=0)
        show_button.grid(row=0, column=1)
        setting_username_button.grid(row=0, column=2)

        self.menu_frame.pack()

    def clear_frames(self):
        if self.add_frame is not None:
            frame = self.add_frame
        elif self.list_frame is not None:
            frame = self.list_frame
        else:
            return
        # destroy all widgets from frame
        # for widget in frame.winfo_children():
        #     widget.destroy()

        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        frame.pack_forget()

    def create_frame_add(self):
        # hide old frames
        self.clear_frames()

        # create widgets

        # self.website_entry.insert(0, self.website_entry.get())

        # add widgets to frame
        self.website_label.grid(row=1, column=0)
        self.website_username.grid(row=2, column=0)
        self.website_password_label.grid(row=3, column=0)

        self.website_entry.grid(row=1, column=1, columnspan=2, padx=ELEMENT_PADX, pady=ELEMENT_PADY)
        self.website_entry.focus()
        self.website_username_entry.grid(row=2, column=1, columnspan=2, padx=ELEMENT_PADX, pady=ELEMENT_PADY)
        if self.website_username_entry.get() == "":
            self.website_username_entry.insert(0, self.file_data["username_default"])
        self.website_password_entry.grid(row=3, column=1, padx=ELEMENT_PADX, pady=ELEMENT_PADY)

        self.generate_password_button.grid(row=3, column=2, padx=ELEMENT_PADX, pady=ELEMENT_PADY)
        self.add_button.grid(row=4, column=1, columnspan=2, padx=ELEMENT_PADX, pady=ELEMENT_PADY)

        # add frame to root window
        self.add_frame.pack()

    def frame_add_button_add_command(self):
        self.file_save()
        self.clear_frames()

    def create_list_frame(self):
        # delete old frames
        self.clear_frames()
        # create frame
        self.list_frame = Frame(self.root)
        # create widgets

        # add frame to root window
        self.list_frame.pack()

    def file_load(self):
        if os.path.isfile(self.data_file_path):
            with open(self.data_file_path, ) as f:
                self.file_data = json.load(f)

    def file_save(self):
        if self.website_entry.get() != "":
            self.file_data["webpages"].append(
                {
                    "webpage": self.website_entry.get(),
                    "username": self.website_password_entry.get(),
                    "password": self.website_password_entry.get()

                })
        with open(self.data_file_path, 'w') as f:
            json.dump(self.file_data, f)

    def run(self):
        self.file_load()
        self.create_menu_frame()
        self.root.mainloop()


app = PasswordManager()
app.run()
