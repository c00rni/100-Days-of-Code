from tkinter import *
from tkinter import ttk
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

csv_dataframe = pd.read_csv("data/french_words.csv")
initial_data = csv_dataframe.sample()


def wrong():
    global initial_data
    canvas.itemconfig(card, image=verso_card_img)
    initial_data = csv_dataframe.sample()
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(text, text=initial_data.values[0][0], fill="black")
    window.after(3000, func=flipCard)
    

def right():
    global initial_data
    canvas.itemconfig(card, image=verso_card_img)
    initial_data = csv_dataframe.sample()
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(text, text=initial_data.values[0][0], fill="black")
    window.after(3000, func=flipCard)


def flipCard():
    canvas.itemconfig(title, text="Créole", fill="white")
    canvas.itemconfig(card, image=recto_card_img)
    canvas.itemconfig(text, text=initial_data.values[0][2], fill="white")

window = Tk()
window.title("Flashy Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flipCard)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

recto_card_img = PhotoImage(file="images/card_back.png")
verso_card_img = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=verso_card_img)
canvas.grid(column=0, row=0, columnspan = 2)

title = canvas.create_text(400, 130, text="French", font=(FONT_NAME, 25, "italic"))
text = canvas.create_text(400, 263, text="data", font=(FONT_NAME, 35, "bold"))


unknow_img = PhotoImage(file="images/wrong.png")
unknow_button = Button(image=unknow_img, highlightthickness=0, command=wrong)
unknow_button.grid(column=0,row=1)


know_img = PhotoImage(file="images/right.png")
know_button = Button(image=know_img, highlightthickness=0, command=right)
know_button.grid(column=1,row=1)

window.mainloop()