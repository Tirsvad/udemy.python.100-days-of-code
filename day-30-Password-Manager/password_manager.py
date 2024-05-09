import json
import secrets
import tkinter as tk
from dataclasses import dataclass
from tkinter import messagebox, simpledialog
import pyperclip

FONT = ("Courier", 12, "normal")
FONT_TITLE = ("Ariel", 32, "normal")
COLOR_TEXT = "#874F51"
COLOR_BG = "#90AEAD"
COLOR_ELEMENT_FOCUS = "#D4483B"
COLOR_ELEMENT = "#FBE9D0"


@dataclass
class DataFileWebPage:
    webpage: str
    username: str
    password: str

    @staticmethod
    def from_dict(obj: dict) -> 'DataFileWebPage':
        """
        populate values from obj: dict

        :param obj: dictionary from json or others
        :return:
        """
        webpage = str(obj.get("webpage"))
        username = str(obj.get("username"))
        password = str(obj.get("password"))
        return DataFileWebPage(webpage=webpage, username=username, password=password)


@dataclass
class DataFile:
    file_data_version: float
    default_username: str
    webpages: list[DataFileWebPage]

    def __init__(self):
        self.webpages = []
        self.file_data_version = 1
        self.default_username = ""

    def from_dict(self, obj: dict) -> 'DataFile':
        """
        populate values from obj: dict

        :param obj: dictionary from json or others
        :return: Datafile
        """
        if int(obj.get("file_data_version")) != int(self.file_data_version):
            raise ValueError(f"File version {obj.get('file_data_version')} is not supported")
        self.default_username = str(obj.get("default_username"))
        file_data_version = int(obj.get("file_data_version"))
        self.webpages = [DataFileWebPage.from_dict(y) for y in obj.get("webpages")]

        if file_data_version != self.file_data_version:
            print(f"File version is not compatible with this version of application")
            raise ValueError
        return DataFile()


# class PasswordManager(tk.Tk):
class PasswordManager:
    window: tk.Tk
    data_file_path: str

    def __init__(self):
        self.window = tk.Tk()
        self.data_file_path = "data.json"

        # Data_file init
        self.data_file = DataFile()
        self.data_file_webpage = DataFileWebPage

        self.data_file.from_dict(self.file_load())

        self.window.option_add("*Background", COLOR_BG)
        self.window.option_add("*Button.Background", COLOR_ELEMENT_FOCUS)

        # all the pages is being created
        self.frames = {}
        container = tk.Frame(self.window)
        container.config(pady=20, padx=20)
        container.grid()

        # iterating through a tuple consisting
        # of the different page layouts
        for page in (StartPage, AddPasswordPage, ListPasswordPage):
            frame = page(container, self)

            # initializing frame of that object from
            # StartPage, AddPasswordPage, ListPasswordPage respectively with
            # for loop
            self.frames[page] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

        self.window.mainloop()

    def show_frame(self, cont):
        """
        To display the current frame
        :param cont:
        :return:
        """
        frame = self.frames[cont]
        frame.update_page()
        frame.tkraise()

    def file_load(self) -> dict:
        """
        Load json file and return data
        :return: data set as dictionary
        """
        try:
            with open(self.data_file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError as e:
            print(f"{e.__str__()}\nWe create file with default values")
            self.file_save()
        except json.decoder.JSONDecodeError as e:
            print(f"{e.msg}\nData file is empty. We create s new file with default values")
            self.file_save()
        return self.data_file.__dict__

    def file_save(self):
        with open(self.data_file_path, 'w') as f:
            json.dump(self.data_file, f, sort_keys=True, indent=4, default=lambda o: o.__dict__)
        messagebox.showinfo(title="Changes added to file", message="File saved")


class CommonPageHeader(tk.Frame):
    title: tk.Canvas.create_text
    canvas: tk.Canvas

    def __init__(self, parent, controller: PasswordManager):
        """

        :param parent: who ever called me!
        :param controller: PasswordManager
        """
        super(CommonPageHeader, parent).__init__()
        self.controller = controller
        self.config(pady=20, padx=20)
        # self.canvas = tk.Canvas(parent, width=600, highlightthickness=1)
        self.canvas = tk.Canvas(parent, width=600, height=200, highlightthickness=0)
        # garbage collection avoid!
        self.canvas.logo = tk.PhotoImage(file="logo.png")
        self.title = self.canvas.create_text(170, 40, text="Common page", font=FONT_TITLE)
        self.canvas.create_image(450, 100, image=self.canvas.logo)
        self.canvas.grid(row=0, column=0, columnspan=3)
        add_button = tk.Button(parent, text="Add new password", width=30,
                               command=lambda: controller.show_frame(AddPasswordPage))
        show_button = tk.Button(parent, text="Show password list", width=30,
                                command=lambda: controller.show_frame(ListPasswordPage))
        setting_username_button = tk.Button(parent, text="Set default username", width=30,
                                            command=lambda: self.set_default_username())

        self.canvas.create_window(50, 100, window=add_button, anchor="w")
        self.canvas.create_window(50, 130, window=show_button, anchor="w")
        self.canvas.create_window(50, 160, window=setting_username_button, anchor="w")

    def update_page(self):
        pass

    def set_default_username(self):
        default_username = simpledialog.askstring(title="Save default username", prompt="Your username you use most")
        if default_username is not None and self.controller.data_file.default_username != default_username:
            self.controller.data_file.default_username = default_username
            self.controller.file_save()
            self.controller.show_frame(StartPage)


class StartPage(CommonPageHeader):
    def __init__(self, parent: tk.Frame, controller: PasswordManager):
        super(StartPage, self).__init__(self, controller)
        self.grid(row=0, column=0)
        self.canvas.itemconfigure(self.title, text="Home")


class AddPasswordPage(CommonPageHeader):
    def __init__(self, parent: tk.Frame, controller: PasswordManager):
        super(AddPasswordPage, self).__init__(self, controller)

        self.default_username = ""
        if controller.data_file.default_username != "":
            self.default_username = controller.data_file.default_username

        self.canvas.itemconfigure(self.title, text="Add password")

        self.grid(row=0, column=0)
        self.add_password_page_webpage_label = tk.Label(self, text="Webpage:", font=FONT)
        self.add_password_page_webpage_entry = tk.Entry(self, width=40)
        self.add_password_page_webpage_search_button = tk.Button(self, text="Search", width=10,
                                                                 command=self.search_password)
        self.add_password_page_username_label = tk.Label(self, text="Email / user name:", font=FONT)
        self.add_password_page_username_entry = tk.Entry(self, width=40)
        self.add_password_page_password_label = tk.Label(self, text="Password:", font=FONT)
        self.add_password_page_password_entry = tk.Entry(self, width=40)

        self.add_password_page_generate_password_button = tk.Button(self, text="Generate password", width=15,
                                                                    command=self.password_generator)
        self.add_password_page_add_button = tk.Button(self, text="Add", width=36, command=lambda: self.add_password())
        self.insert_default_values()

        # Create the grid
        self.add_password_page_webpage_label.grid(row=6, column=0)
        self.add_password_page_webpage_entry.grid(row=6, column=1, columnspan=2, pady=3, padx=3, sticky="W")
        self.add_password_page_webpage_search_button.grid(row=6, column=2, pady=3, padx=3, sticky="E")
        self.add_password_page_username_label.grid(row=7, column=0)
        self.add_password_page_username_entry.grid(row=7, column=1, columnspan=2, pady=3, padx=3, sticky="W")
        self.add_password_page_password_label.grid(row=8, column=0)
        self.add_password_page_password_entry.grid(row=8, column=1, pady=3, padx=3, sticky="W")
        self.add_password_page_generate_password_button.grid(row=8, column=2, pady=3, padx=3, sticky="E")
        self.add_password_page_add_button.grid(row=9, columnspan=3, pady=3, padx=3)

    def insert_default_values(self):
        self.add_password_page_username_entry.delete(0, tk.END)
        self.add_password_page_username_entry.insert(0, self.default_username)

    def add_password(self):
        error_msg = ""

        # validation
        if self.add_password_page_webpage_entry.get() == "":
            error_msg += "Webpage is not filled\n"
        if self.add_password_page_username_entry.get() == "":
            error_msg += "Username is not filled\n"
        if self.add_password_page_password_entry.get() == "":
            error_msg += "Password is not filled\n"
        if error_msg:
            messagebox.showwarning(title="Required input fields not filled", message=error_msg)
            return

        # see if it already exists
        for i in range(0, len(self.controller.data_file.webpages)):
            if self.controller.data_file.webpages[i].webpage.lower() == \
                    self.add_password_page_webpage_entry.get().lower() and \
                    self.controller.data_file.webpages[i].username.lower() == \
                    self.add_password_page_username_entry.get().lower():
                if messagebox.askyesno(title="Data entry already exists",
                                       message=f"Overwrite existing password for {self.controller.data_file.webpages[i].webpage}"):
                    self.controller.data_file.webpages[i].password = self.add_password_page_password_entry.get()
                    self.controller.file_save()
                self.clear()
                return

        # data class data_webpage is populate
        data_webpage = DataFileWebPage(
            webpage=self.add_password_page_webpage_entry.get().title(),
            username=self.add_password_page_username_entry.get(),
            password=self.add_password_page_password_entry.get()
        )
        self.controller.data_file.webpages.append(data_webpage)

        self.controller.file_save()

        # clear entry fields
        self.clear()

    def password_generator(self, length=12):
        self.add_password_page_password_entry.delete(0, tk.END)
        password = secrets.token_urlsafe(length)
        self.add_password_page_password_entry.insert(0, password)
        pyperclip.copy(self.add_password_page_password_entry.get())

    def search_password(self):
        webpage_entry = self.add_password_page_webpage_entry.get()
        i = []
        # TODO
        for index in range(0, len(self.controller.data_file.webpages)):
            if self.controller.data_file.webpages[index].webpage == webpage_entry.title():
                i.append(index)
        if len(i) == 0:
            messagebox.showwarning(title="Not found", message="Website is not found")
            return
        elif len(i) == 2:
            messagebox.showinfo(title="Multiple found",
                                message="More than 1 entry found. Use <show password list> instead")
            return
        pyperclip.copy(self.controller.data_file.webpages[i[0]].password)
        messagebox.showinfo(title="Your password",
                            message=f"webpage: {self.controller.data_file.webpages[i[0]].webpage}\n"
                                    f"username: {self.controller.data_file.webpages[i[0]].username}\n"
                                    f"password: {self.controller.data_file.webpages[i[0]].password}")

    def clear(self):
        self.add_password_page_webpage_entry.delete(0, tk.END)
        self.add_password_page_username_entry.delete(0, tk.END)
        self.add_password_page_username_entry.insert(0, self.default_username)
        self.add_password_page_password_entry.delete(0, tk.END)

    def update_page(self):
        if self.controller.data_file.default_username:
            self.default_username = self.controller.data_file.default_username
            self.insert_default_values()


class ListPasswordPage(CommonPageHeader):
    def __init__(self, parent: tk.Frame, controller: PasswordManager):
        super(ListPasswordPage, self).__init__(self, controller)
        self.grid(row=0, column=0)
        self.canvas.itemconfigure(self.title, text="List password")
        self.frame_body = tk.Frame(self)
        # self.frame_body.config(width=140)
        self.frame_body.grid(row=6, column=0, columnspan=3)
        self.e = None
        self.update()

    def update_page(self):
        i = 0

        self.e = tk.Entry(self.frame_body)
        self.e.insert(tk.END, "Webpage")
        self.e.grid(row=i + 7, column=0)

        self.e = tk.Entry(self.frame_body)
        self.e.insert(tk.END, "Username")
        self.e.grid(row=i + 7, column=1)

        self.e = tk.Entry(self.frame_body)
        self.e.insert(tk.END, "Password")
        self.e.grid(row=i + 7, column=2)

        for webpage in self.controller.data_file.webpages:
            i += 1
            self.e = tk.Entry(self.frame_body)
            self.e.insert(tk.END, webpage.webpage)
            self.e.grid(row=i + 7, column=0)
            self.e = tk.Entry(self.frame_body)
            self.e.insert(tk.END, webpage.username)
            self.e.grid(row=i + 7, column=1)
            self.e = tk.Entry(self.frame_body)
            self.e.insert(tk.END, webpage.password)
            self.e.grid(row=i + 7, column=2)
