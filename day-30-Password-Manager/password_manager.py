import json
import secrets
import tkinter as tk
from dataclasses import dataclass
from tkinter import messagebox, simpledialog
import pyperclip

FONT = ("Courier", 12, "normal")
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
        _password = str(obj.get("password"))
        _username = str(obj.get("username"))
        _webpage = str(obj.get("webpage"))
        return DataFileWebPage(_password, _username, _webpage)


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
        _file_data_version = int(obj.get("file_data_version"))
        self.webpages = [DataFileWebPage.from_dict(y) for y in obj.get("webpages")]

        if _file_data_version != self.file_data_version:
            print(f"File version is not compatible with this version of application")
            raise ValueError
        return DataFile()


class PasswordManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.data_file_path = "data.json"

        # Data_file init
        self.data_file = DataFile()
        self.data_file_webpage = DataFileWebPage

        self.data_file.from_dict(self.file_load())

        self.option_add("*Background", COLOR_BG)
        self.option_add("*Button.Background", COLOR_ELEMENT_FOCUS)

        # all the pages is being created
        self.frames = {}
        container = tk.Frame(self)
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
            print(f"file save data {self.data_file}")
            json.dump(self.data_file, f, sort_keys=True, indent=4, default=lambda o: o.__dict__)
        messagebox.showinfo(title="Changes added to file", message="File saved")


class CommonPageHeader(tk.Frame):
    def __init__(self, parent, controller: PasswordManager):
        """

        :param parent: who ever called me!
        :param controller: PasswordManager
        """
        super(CommonPageHeader, parent).__init__()
        self.controller = controller
        self.config(pady=20, padx=20)

        canvas = tk.Canvas(parent, width=200, height=200, highlightthickness=0)
        # garbage collection avoid!
        canvas.logo = tk.PhotoImage(file="logo.png")
        canvas.create_image(100, 100, image=canvas.logo)
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
        self.start_page_label = tk.Label(self, text="Home", font=FONT)
        self.start_page_label.grid(row=0, columnspan=3)


class AddPasswordPage(CommonPageHeader):
    def __init__(self, parent: tk.Frame, controller: PasswordManager):
        super(AddPasswordPage, self).__init__(self, controller)

        self.default_username = ""
        if controller.data_file.default_username != "":
            self.default_username = controller.data_file.default_username

        self.grid(row=0, column=0)
        self.add_password_page_label = tk.Label(self, text="Add password", font=FONT)
        self.add_password_page_webpage_label = tk.Label(self, text="Webpage:", font=FONT)
        self.add_password_page_webpage_entry = tk.Entry(self, width=29)
        self.add_password_page_webpage_search_button = tk.Button(self, text="Search", width=10,
                                                                 command=self.search_webpage)
        self.add_password_page_username_label = tk.Label(self, text="Email / user name:", font=FONT)
        self.add_password_page_username_entry = tk.Entry(self, width=43)
        self.add_password_page_password_label = tk.Label(self, text="Password:", font=FONT)
        self.add_password_page_password_entry = tk.Entry(self, width=23)

        self.add_password_page_generate_password_button = tk.Button(self, text="Generate password", width=15,
                                                                    command=self.password_generator)
        self.add_password_page_add_button = tk.Button(self, text="Add", width=36, command=lambda: self.add_password())
        self.insert_default_values()

        # Create the grid
        self.add_password_page_label.grid(row=0, column=0, columnspan=3)
        self.add_password_page_webpage_label.grid(row=6, column=0)
        self.add_password_page_webpage_entry.grid(row=6, column=1, columnspan=2, pady=3, padx=3, sticky="W")
        self.add_password_page_webpage_search_button.grid(row=6, column=2, pady=3, padx=3, sticky="E")
        self.add_password_page_username_label.grid(row=7, column=0)
        self.add_password_page_username_entry.grid(row=7, column=1, columnspan=2, pady=3, padx=3)
        self.add_password_page_password_label.grid(row=8, column=0)
        self.add_password_page_password_entry.grid(row=8, column=1, pady=3, padx=3)
        self.add_password_page_generate_password_button.grid(row=8, column=2, pady=3, padx=3)
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

        # data class data_webpage is populate
        data_webpage = DataFileWebPage(
            webpage=self.add_password_page_webpage_entry.get(),
            username=self.add_password_page_username_entry.get(),
            password=self.add_password_page_password_entry.get()
        )
        self.controller.data_file.webpages.append(data_webpage)

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

    def search_webpage(self):
        webpage_entry = self.add_password_page_webpage_entry.get()
        i = []
        # TODO
        print(f"webpage_entry {webpage_entry}")
        print(f"length {len(self.controller.data_file.webpages)}")
        for index in range(0, len(self.controller.data_file.webpages)):
            if self.controller.data_file.webpages[index].webpage == webpage_entry:
                i.append(index)
                print(self.controller.data_file.webpages[index].webpage)

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
        self.start_page_label = tk.Label(self, text="List passwords", font=FONT)
        self.start_page_label.grid(row=0, columnspan=3)
