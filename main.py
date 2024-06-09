from tkinter import *

MAIN_BG = "white"
MAIN_FG = "black"
FONT = ("Arial", 14, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=MAIN_BG)

canvas = Canvas(width=200, height=200, bg=MAIN_BG, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:", bg=MAIN_BG, fg=MAIN_FG, font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=40, bg=MAIN_BG, highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2)

# Email/Username
username_label = Label(text="Email/Username:", bg=MAIN_BG, fg=MAIN_FG, font=FONT)
username_label.grid(row=2, column=0)

username_entry = Entry(width=40, bg=MAIN_BG, highlightthickness=0)
username_entry.grid(row=2, column=1, columnspan=2)

# Password
password_label = Label(text="Password:", bg=MAIN_BG, fg=MAIN_FG, font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=22, bg=MAIN_BG, highlightthickness=0)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", highlightbackground=MAIN_BG)
generate_password_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", highlightbackground=MAIN_BG, width=37)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
