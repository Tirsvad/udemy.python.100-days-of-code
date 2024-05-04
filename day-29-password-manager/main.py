import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os.path
import secrets
import pyperclip

FONT = ("Courier", 12, "normal")
COLOR_TEXT = "#874F51"
COLOR_BG = "#90AEAD"
COLOR_ELEMENT_FOCUS = "#D4483B"
COLOR_ELEMENT = "#FBE9D0"


class PasswordManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.data_file_path = "data.json"
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
        self.file_load()
        self.title("Password Manager")
        self.option_add("*Background", COLOR_BG)
        self.option_add("*Button.Background", COLOR_ELEMENT_FOCUS)
        container = tk.Frame(self)
        container.config(pady=20, padx=20)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, AddPasswordPage, ListPasswordPage):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        """
        to display the current frame passed as parameter
        :param cont:
        :return:
        """
        frame = self.frames[cont]
        frame.tkraise()

    def add_password(self):
        self.file_save()

    def file_load(self):
        if os.path.isfile(self.data_file_path):
            with open(self.data_file_path, ) as f:
                self.file_data = json.load(f)

    def file_save(self):
        if self.frames[AddPasswordPage].add_password_page_webpage_entry.get() != "":
            self.file_data["webpages"].append({
                "webpage": self.frames[AddPasswordPage].add_password_page_webpage_entry.get(),
                "username": self.frames[AddPasswordPage].add_password_page_username_entry.get(),
                "password": self.frames[AddPasswordPage].add_password_page_password_entry.get(),
            })
        with open(self.data_file_path, 'w') as f:
            json.dump(self.file_data, f, sort_keys=True, indent=4)
        messagebox.showinfo(title="Password added to file", message="Password saved")


class PageHeader(tk.Frame):
    def __init__(self, parent, controller: PasswordManager):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(parent, width=200, height=200, highlightthickness=0)
        # garbage collection avoid!
        canvas.test = tk.PhotoImage(file="logo.png")
        canvas.create_image(100, 100, image=canvas.test)
        add_button = tk.Button(parent, text="Add new password", width=30,
                               command=lambda: controller.show_frame(AddPasswordPage))
        show_button = tk.Button(parent, text="Show your passwords", width=30,
                                command=lambda: controller.show_frame(ListPasswordPage))
        setting_username_button = tk.Button(parent, text="Set default username", width=30)
        canvas.grid(row=1, column=1, columnspan=2, rowspan=5)

        add_button.grid(row=1, column=0, padx=5, pady=5)
        show_button.grid(row=2, column=0, padx=5, pady=5)
        setting_username_button.grid(row=3, column=0, padx=5, pady=5)

    def clear(self):
        pass


class StartPage(tk.Frame):

    def __init__(self, parent, controller: PasswordManager):
        tk.Frame.__init__(self, parent)
        PageHeader(self, controller)
        self.startpage_label = tk.Label(self, text="Homepage", font=FONT)
        self.startpage_label.grid(row=0, columnspan=3)

    def clear(self):
        pass


class AddPasswordPage(tk.Frame):

    def __init__(self, parent, controller: PasswordManager):
        tk.Frame.__init__(self, parent)
        PageHeader(self, controller)
        self.controller = controller
        self.default_username = ""
        if controller.file_data["username_default"]:
            self.default_username = controller.file_data["username_default"]

        self.add_password_page_label = tk.Label(self, text="Add password page", font=FONT)
        self.add_password_page_webpage_label = tk.Label(self, text="Webpage:", font=FONT)
        self.add_password_page_webpage_entry = tk.Entry(self, width=43)
        self.add_password_page_username_label = tk.Label(self, text="Email / user name:", font=FONT)
        self.add_password_page_username_entry = tk.Entry(self, width=43)
        self.add_password_page_password_label = tk.Label(self, text="Password:", font=FONT)
        self.add_password_page_password_entry = tk.Entry(self, width=23)
        self.add_password_page_generate_password_button = tk.Button(self, text="Generate password", width=15,
                                                                    command=self.password_generator)
        self.add_password_page_add_button = tk.Button(self, text="Add", width=36, command=lambda: self.add_password())
        self.insert_default_values()

        # put widgets to frame
        self.add_password_page_label.grid(row=0, column=0, columnspan=3)
        self.add_password_page_webpage_label.grid(row=6, column=0)
        self.add_password_page_webpage_entry.grid(row=6, column=1, columnspan=2, pady=3, padx=3)
        self.add_password_page_username_label.grid(row=7, column=0)
        self.add_password_page_username_entry.grid(row=7, column=1, columnspan=2, pady=3, padx=3)
        self.add_password_page_password_label.grid(row=8, column=0)
        self.add_password_page_password_entry.grid(row=8, column=1, pady=3, padx=3)
        self.add_password_page_generate_password_button.grid(row=8, column=2, pady=3, padx=3)
        self.add_password_page_add_button.grid(row=9, columnspan=3, pady=3, padx=3)

    def insert_default_values(self):
        self.add_password_page_username_entry.insert(0, self.default_username)

    def add_password(self):
        error_msg = ""
        if self.add_password_page_webpage_entry.get() == "":
            error_msg += "Webpage is not filled\n"
        if self.add_password_page_username_entry.get() == "":
            error_msg += "Username is not filled\n"
        if self.add_password_page_password_entry.get() == "":
            error_msg += "Password is not filled\n"
        if error_msg:
            messagebox.showwarning(title="Required input fields not filled", message=error_msg)
            return
        self.controller.file_save()

        # clear entry fields
        self.add_password_page_webpage_entry.delete(0, tk.END)
        self.add_password_page_username_entry.delete(0, tk.END)
        self.add_password_page_password_entry.delete(0, tk.END)
        self.insert_default_values()

    def password_generator(self, length=12):
        self.add_password_page_password_entry.delete(0, tk.END)
        password = secrets.token_urlsafe(length)
        self.add_password_page_password_entry.insert(0, password)
        pyperclip.copy(self.add_password_page_password_entry.get())

    def set_default_username(self):
        self.controller.file_data["username_default"] = simpledialog.askstring(title="Default username",
                                                                               prompt="Your most common username / "
                                                                                      "email?")

    def clear(self):
        self.add_password_page_webpage_entry.delete(0, tk.END)
        self.add_password_page_username_entry.delete(0, tk.END)
        self.add_password_page_username_entry.insert(0, self.default_username)
        self.add_password_page_password_entry.delete(0, tk.END)


class ListPasswordPage(tk.Frame):
    def __init__(self, parent, controller: PasswordManager):
        tk.Frame.__init__(self, parent)
        PageHeader(self, controller)
        self.controller = controller
        self.list_password_page_label = tk.Label(self, text="List password", font=FONT)
        self.list_password_page_label.grid(row=0, column=0, columnspan=3)
        self.frame_body = tk.Frame(self)
        self.frame_body.grid(row=6, column=0, columnspan=3)
        # tk list table
        self.file_data = controller.file_data
        for i in range(len(self.file_data["webpages"]) + 1):
            for j in range(3):
                self.e = tk.Entry(self.frame_body)
                if i == 0:
                    if j == 0:
                        self.e.insert(tk.END, "Webpage")
                    if j == 1:
                        self.e.insert(tk.END, "Username")
                        self.e.config(width=35)
                    if j == 2:
                        self.e.insert(tk.END, "password")
                else:
                    if j == 0:
                        self.e.insert(tk.END, self.file_data["webpages"][i - 1]["webpage"])
                    if j == 1:
                        self.e.insert(tk.END, self.file_data["webpages"][i - 1]["username"])
                        self.e.config(width=35)
                    if j == 2:
                        self.e.insert(tk.END, self.file_data["webpages"][i - 1]["password"])
                self.e.grid(row=i + 7, column=j)


app = PasswordManager()
app.mainloop()
