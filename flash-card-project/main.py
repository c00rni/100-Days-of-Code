BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# TODO: Use the images in the image folder, to create the interface. Add images and button

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Flashy Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

verso_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=verso_card_img)
canvas.grid(column=0, row=0, columnspan = 2)

title = canvas.create_text(400, 130, text="French", font=(FONT_NAME, 25, "italic"))
text = canvas.create_text(400, 263, text="text", font=(FONT_NAME, 35, "bold"))


unknow_img = PhotoImage(file="images/wrong.png")
unknow_button = Button(image=unknow_img, highlightthickness=0)
unknow_button.grid(column=0,row=1)


know_img = PhotoImage(file="images/right.png")
know_button = Button(image=know_img, highlightthickness=0)
know_button.grid(column=1,row=1)




"""wrong_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=wrong_img)
canvas.grid(column=0, row=0, columnspan = 2)

right_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)"""



window.mainloop()