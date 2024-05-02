import tkinter


def button_clicked():
    my_label.config(text="I got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My GUI")
window.minsize(width=800, height=600)
window.config(padx=10, pady=10)

my_label = tkinter.Label(text="I love python", font=("Arial", 14, "bold"))
my_label.config(padx=10, pady=10)
my_label.grid(column=0, row=0)


my_button = tkinter.Button(text="click me", command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.grid(column=1, row=1)


my_input = tkinter.Entry(width=10)
my_input.grid(column=3, row=2)


new_button = tkinter.Button(text="new  buttonn", command=button_clicked)
# new_button.config(padx=10, pady=10)
new_button.grid(column=2, row=0)


window.mainloop()