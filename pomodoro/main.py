
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=264, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 132, image=tomato_img)
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Serif", 50, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)


canvas.create_text(105, 145, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()