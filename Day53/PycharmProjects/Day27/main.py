from tkinter import  *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def btn_clicked():
    print("I got clicked")
    new_text = input_case.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="My new Label", font=("Arial", 20, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button
my_button = Button(text="Click Me", command=btn_clicked)
my_button.grid(column=1, row=1)
my_button.config(padx=20, pady=20)

my_button = Button(text="Click Me", command=btn_clicked)
my_button.grid(column=2, row=0)

# Entry
input_case = Entry(width=30)
print(input_case.get())
input_case.grid(column=3, row=2)


window.mainloop()
