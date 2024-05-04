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
        container.grid() #(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

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
        frame.update_page()
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
        messagebox.showinfo(title="Changes added to file", message="Changes saved")


class PageHeader(tk.Frame):
    def __init__(self, parent, controller: PasswordManager):
        super(PageHeader, parent).__init__()
        self.controller = controller
        self.config(pady=20, padx=20)
        # self.frame_head_body = tk.Frame(parent)
        # super().__init__(self, parent)

        canvas = tk.Canvas(parent, width=200, height=200, highlightthickness=0)
        # garbage collection avoid!
        canvas.test = tk.PhotoImage(file="logo.png")
        canvas.create_image(100, 100, image=canvas.test)
        add_button = tk.Button(parent, text="Add new password", width=30,
                               command=lambda: controller.show_frame(AddPasswordPage))
        show_button = tk.Button(parent, text="Show your passwords", width=30,
                                command=lambda: controller.show_frame(ListPasswordPage))
        setting_username_button = tk.Button(parent, text="Set default username", width=30,
                                            command=lambda: self.set_default_username())
        canvas.grid(row=1, column=1, columnspan=2, rowspan=4)

        add_button.grid(row=1, column=0, padx=5, pady=4)
        show_button.grid(row=2, column=0, padx=5, pady=4)
        setting_username_button.grid(row=3, column=0, padx=5, pady=4)

    def set_default_username(self):
        username = ""
        username = simpledialog.askstring(title="Default username", prompt="Your most common username / email?")
        if username:
            self.controller.file_data["username_default"] = username
            self.controller.file_save()
        self.controller.show_frame(StartPage)

    def update_page(self):
        pass


class StartPage(PageHeader):

    def __init__(self, parent: tk.Frame, controller: PasswordManager):

        super(StartPage, self).__init__(self, controller)
        self.grid(row=0, column=0)

        # PageHeader(self, controller)
        self.startpage_label = tk.Label(self, text="Homepage", font=FONT)
        self.startpage_label.grid(row=0, columnspan=3)


class AddPasswordPage(PageHeader):

    def __init__(self, parent, controller: PasswordManager):
        super(AddPasswordPage, self).__init__(self, controller)
        self.frame_body = tk.Frame(self)
        self.default_username = ""
        if controller.file_data["username_default"]:
            self.default_username = controller.file_data["username_default"]
        self.add_password_page_label = tk.Label(self, text="Add password", font=FONT)
        self.add_password_page_webpage_label = tk.Label(self.frame_body, text="Webpage:", font=FONT)
        self.add_password_page_webpage_entry = tk.Entry(self.frame_body, width=43)
        self.add_password_page_username_label = tk.Label(self.frame_body, text="Email / user name:", font=FONT)
        self.add_password_page_username_entry = tk.Entry(self.frame_body, width=43)
        self.add_password_page_password_label = tk.Label(self.frame_body, text="Password:", font=FONT)
        self.add_password_page_password_entry = tk.Entry(self.frame_body, width=23)
        self.add_password_page_generate_password_button = tk.Button(self.frame_body, text="Generate password", width=15,
                                                                    command=self.password_generator)
        self.add_password_page_add_button = tk.Button(self.frame_body, text="Add", width=36, command=lambda: self.add_password())
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
        self.frame_body.grid(row=5, columnspan=3)

    def insert_default_values(self):
        self.add_password_page_username_entry.delete(0, tk.END)
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

    def clear(self):
        self.add_password_page_webpage_entry.delete(0, tk.END)
        self.add_password_page_username_entry.delete(0, tk.END)
        self.add_password_page_username_entry.insert(0, self.default_username)
        self.add_password_page_password_entry.delete(0, tk.END)

    def update_page(self):
        if self.controller.file_data["username_default"]:
            self.default_username = self.controller.file_data["username_default"]
            self.insert_default_values()


class ListPasswordPage(PageHeader):
    def __init__(self, parent, controller: PasswordManager):
        super(ListPasswordPage, self).__init__(self, controller)
        self.frame_body = tk.Frame(self)
        self.controller = controller
        self.list_password_page_label = tk.Label(self, text="List password", font=FONT)
        self.list_password_page_label.grid(row=0, column=0, columnspan=3)
        self.frame_body = tk.Frame(self)
        self.frame_body.grid(row=6, column=0, columnspan=3)
        self.file_data = self.controller.file_data
        self.update()

    def update_page(self):
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
