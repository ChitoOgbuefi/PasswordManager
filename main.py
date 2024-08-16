from tkinter import messagebox
import pyperclip
from tkinter import *
from random import *
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    character_bank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4',
                      '5', '6', '7', '8', '9''!', '#', '$', '%', '&', '(', ')', '*', '+']

    key = [choice(character_bank) for item in range(randint(12, 15))]
    key = "".join(key)
    password_input.delete(0, END)
    password_input.insert(0, key)
    pyperclip.copy(key)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_data = {
        website_input.get(): {
            "email": username_input.get(),
            "password": password_input.get(),
        }
    }

    if username_input.get() == "" or password_input.get() == "":
        messagebox.showerror(title="Error", message="Please don't leave any fields open!")
    else:
        is_ok = messagebox.askokcancel(message=f"These are the details entered:\n"
                                               f"Website: {website_input.get()}\n"
                                               f"Username: {username_input.get()}\n"
                                               f"Password: {password_input.get()}")
        if is_ok:
            try:
                with open("data.json", "r") as passwords:
                    # Read old data
                    data = json.load(passwords)

            except FileNotFoundError:
                with open("data.json", "w") as passwords:
                    # Save updated data
                    json.dump(new_data, passwords, indent=4)
                    messagebox.showerror(title="Update", message="New file created!")
            else:
                # Update old data with new data
                data.update(new_data)

                with open("data.json", "w") as passwords:
                    # Save updated data
                    json.dump(data, passwords, indent=4)

            finally:
                # Delete text after adding password
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    try:
        with open("data.json", "r") as passwords:
            data = json.load(passwords)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website_input.get() in data:
            messagebox.showinfo(message=f"Website: {website_input.get()}\n"
                                        f"Email: {data[website_input.get()]['email']}\n"
                                        f"Password: {data[website_input.get()]["password"]}")
        else:
            messagebox.showinfo(title="Error", message="No data found!")


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Label
website = Label(text="Website:", bg="white", fg="black", font=("Arial", 15))
website.grid(column=0, row=1)
username = Label(text="Email/Username:", bg="white", fg="black", font=("Arial", 15))
username.grid(column=0, row=2)
password = Label(text="Password:", bg="white", fg="black", font=("Arial", 15))
password.grid(column=0, row=3)

# Input
website_input = Entry(width=22, bg="white", fg="black", highlightbackground="white")
website_input.grid(column=1, row=1)
website_input.focus()
username_input = Entry(width=39, bg="white", fg="black", highlightbackground="white")
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "ClarenceOgbuefi@gmail.com")
password_input = Entry(width=22, bg="white", fg="black", highlightbackground="white")
password_input.grid(column=1, row=3)

# Buttons
generate_password = Button(text="Generate Password", highlightbackground="white", command=password_generator)
generate_password.grid(column=2, row=3)
add = Button(text="Add", width=37, highlightbackground="white", command=save)
add.grid(column=1, row=4, columnspan=2)
search_info = Button(text="Search", highlightbackground="white", command=search, width=13)
search_info.grid(column=2, row=1)

window.mainloop()
