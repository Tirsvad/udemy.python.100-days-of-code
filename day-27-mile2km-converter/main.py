from tkinter import Tk, Label, Entry, Button

FONT = ("Arial", 12, "normal")


def button_clicked():
    result = float(my_entry.get()) * 1.609344
    label_result.config(text=f"{result:,.02f}")


window = Tk()
window.title("Mile to km converter")
window.config(padx=20, pady=20)

label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0, pady=5, padx=5, sticky="w")

label_equal = Label(text="is equal to", font=FONT)
label_equal.grid(column=0, row=1, pady=5, padx=5)

label_result = Label(text="0", font=FONT)
label_result.grid(column=1, row=1, pady=5, padx=5)

label_km = Label(text="Km", font=FONT)
label_km.grid(column=2, row=1, pady=5, padx=5, sticky="w")

my_entry = Entry(width=10)
my_entry.grid(column=1, row=0, pady=5, padx=5)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2, pady=5, padx=5)

window.mainloop()
