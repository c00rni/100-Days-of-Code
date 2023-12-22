# ---------------------------- PASSWORD GENERATOR #------------------------------- #

# ---------------------------- SAVE PASSWORD #------------------------------- #

# ---------------------------- UI SETUP 

from tkinter import *

BASE_SIZE = 40

root = Tk()
root.config(highlightthickness=0, padx=50, pady=40)
print(root.configure().keys())

# Title = Password Mnager
root.title("Password Manager")


# Canvas with a image (200 x 189)
canvas = Canvas(width=200, height=260, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 144, image=logo_img)
canvas.grid(column=1, row=0, columnspan = 2)

# site_label "Website:"
site_label = Label(text="Website:")
site_label.grid(column=0, row=1)

# site_input
site_input = Entry(width=BASE_SIZE)
site_input.grid(column=1, row=1, columnspan = 2)

# user_name_label "Email/Username:"
user_name_label = Label(text="Email/Username:")
user_name_label.grid(column=0, row=2, )

# user_name_input
user_name_input = Entry(width=BASE_SIZE)
user_name_input.grid(column=1, row=2, columnspan = 2)

# password_label "Password:"
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# password_input
password_input = Entry(width=BASE_SIZE // 2 -1)
password_input.grid(column=1, row=3)

# generator_button
generator_button = Button(text="Generate Password", width=BASE_SIZE // 2 -1)
generator_button.grid(column=2, row=3)

# add_button "Add"
generator_button = Button(text="Generate Password", width=BASE_SIZE)
generator_button.grid(column=1, row=4, columnspan = 2)

root.mainloop()

#------------------------------- #