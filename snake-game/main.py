from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snack = Snake()

screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.right, "Right")
screen.onkey(snack.left, "Left")

game_is_on = True
while game_is_on:
    snack.move()
    screen.update()
    time.sleep(0.1)
    
screen.mainloop()
