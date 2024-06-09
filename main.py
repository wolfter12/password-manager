from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email/Username
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2)

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", width=37)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
