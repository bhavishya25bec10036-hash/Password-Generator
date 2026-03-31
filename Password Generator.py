from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    input_password.delete(0, END)
    input_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    name_website = input_website.get()
    name_email = input_email.get()
    name_password = input_password.get()

    if len(name_website) == 0 or len(name_email) <= 3 or len(name_password) == 0:
        messagebox.showinfo(title="Uhh-ohh", message="Oops missed a field")
        return

    is_ok = messagebox.askokcancel(title="Confirm",
                                   message=f"Website: {name_website}\nEmail: {name_email}\nPassword: {name_password}\nSave?")
    if is_ok:
        with open('password.txt', 'a') as data:
            data.write(f"{name_website} || {name_email} || {name_password}\n")

        messagebox.showinfo(title="Success", message="Successfully Saved")
        input_password.delete(0, END)
        input_website.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(bg='white', padx=50, pady=50)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=0, column=0)

input_website = Entry(width=50)
input_website.grid(row=0, column=1, columnspan=2)
input_website.focus()

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=1, column=0)

input_email = Entry(width=50)
input_email.grid(row=1, column=1, columnspan=2)
input_email.insert(0, "yourname@gmail.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(row=2, column=0)

input_password = Entry(width=25)
input_password.grid(row=2, column=1)

password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(row=2, column=2)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=3, column=1, columnspan=2)

window.mainloop()