from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="My new Label", font=("Arial", 20, "bold"))
my_label.pack()

my_label["text"] = "Label changed using key"
my_label.config(text="changed using general")

# Button
def btn_clicked():
    print("I got clicked")


my_button = Button(text="Click Me", command=btn_clicked)
my_button.pack()

# Entry
input_case = Entry(width=30)
input_case.insert(END, string="Some text as default")
print(input_case.get())
input_case.pack()

# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example text multiline")
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_fun():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, command=spinbox_fun)
spinbox.pack()


# Scale
def scale_fun(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_fun)
scale.pack()


# Checkbutton
def check_fun():
    print(check_state.get())


check_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=check_state, command=check_fun)
check_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox()
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
