from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_input_case.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_input_case.get().title()
    email = email_input_case.get()
    password = pass_input_case.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure that you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=f"For - {website.title()}", message=f"This are the details entered: "
                                                    f"\n Email: {email} \n Password: {password} \n Is it okay?")

        if is_ok:
            try: # trying to catch a bock that may fail
                with open("data_sites.json", "r") as saved:
                    data = json.load(saved)
            except FileNotFoundError: # -catches that block when it fails
                with open("data_sites.json", "w") as saved:
                    json.dump(new_data, saved, indent=4)
            except JSONDecodeError:
                messagebox.showinfo(title=f"Error", message="Can't update cause file is empty")
            else: # runs when the block does not have an error
                data.update(new_data)

                with open("data_sites.json", "w") as saved:
                    json.dump(data, saved, indent=4)
            finally: # runs no matter the outcome be it an error or not
                web_input_case.delete(0, END)
                pass_input_case.delete(0, END)


# ---------------------------- SEARCH SECTION ------------------------------- #
def find_password():
    website = web_input_case.get().title()
    try:
        with open("data_sites.json", "r") as saved:
            data = json.load(saved)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message="No Data File Found")
    except JSONDecodeError:
        messagebox.showinfo(title=f"Error", message="No Data File have been created")
    else:
        if website in data:
            web_data = data[website]
            email_data = web_data["email"]
            password_data = web_data["password"]
            messagebox.showinfo(title=f"{website}", message=f"Your Email is: {email_data} \n Password is: {password_data}")
        else:
            messagebox.showinfo(title=f"Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label1
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

# Entry1
web_input_case = Entry(width=32)
web_input_case.focus()
web_input_case.grid(row=1, column=1)

# search_btn
search_btn = Button(text="Search", width=7, command=find_password)
search_btn.grid(row=1, column=2)

# Label2
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

# Entry2
email_input_case = Entry(width=42)
email_input_case.insert(0, "learn@gmail.com")
email_input_case.grid(row=2, column=1, columnspan=2)

# Label3
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry3
pass_input_case = Entry(width=32)
pass_input_case.grid(row=3, column=1)

# Button1
btn_generate = Button(text="Generate", width=7, command=generate_password)
btn_generate.grid(row=3, column=2)

# Button2
btn_add = Button(text="Add", width=36, command=save_password)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
