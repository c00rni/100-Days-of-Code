import time
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
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def startTimer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countDown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=("Serif", 50, "bold"))
    elif reps % 2 == 0:
        countDown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=("Serif", 50, "bold"))
    else:
        countDown(WORK_MIN  * 60)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=("Serif", 50, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countDown(count):
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(counter, text=f"{min}:{sec}")
    if count > 0:
        window.after(1000, countDown, count - 1)
    else:
        startTimer()
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, print)

canvas = Canvas(width=210, height=264, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 132, image=tomato_img)
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Serif", 50, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=startTimer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)


counter = canvas.create_text(105, 145, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()