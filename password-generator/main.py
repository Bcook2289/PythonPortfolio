from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


def generate_password():

    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for p in range(randint(8, 10))]
    password_symbols = [choice(symbols) for q in range(randint(2, 4))]
    password_numbers = [choice(numbers) for r in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(END, password)
    pyperclip.copy(password)

def save():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any blank fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details Entered: \nEmail: {website}"
                                                              f"\nPassword: {password}\nSave?")
        if is_ok:
            file = open("data.txt", "a")
            file.write(f"\n{website} | {username} | {password}")
            file.close()
            website_input.delete(0, END)
            password_input.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
window_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=window_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

username_input = Entry(width=35)
username_input.insert(END, "email")
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")

password_input = Entry(width=30)
password_input.grid(column=1, row=3, sticky="W")

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)

add_pass = Button(text="Add", width=30, command=save)
add_pass.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
