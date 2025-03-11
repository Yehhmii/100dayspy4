from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=20)


def btn_clicked():
    new_text = float(input_case.get())
    km = round(new_text * 1.609)
    my_label3.config(text=km)


# Entry
input_case = Entry(width=10)
input_case.insert(END, string="0")
input_case.get()
input_case.grid(column=1, row=0)

# Label
my_label = Label(text="Miles", font=("Arial", 10, "bold"))
my_label.grid(column=2, row=0)

# Label
my_label2 = Label(text="is equal to", font=("Arial", 10, "bold"))
my_label2.grid(column=0, row=1)

# Label
my_label3 = Label(text="0", font=("Arial", 10, "bold"))
my_label3.grid(column=1, row=1)

# Label
my_label4 = Label(text="Km", font=("Arial", 10, "bold"))
my_label4.grid(column=2, row=1)

# Button
my_button = Button(text="Click Me", command=btn_clicked)
my_button.grid(column=1, row=2)


window.mainloop()
