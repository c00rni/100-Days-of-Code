from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


snack_body = []
for i in range(3):
    square = Turtle()
    square.shapesize(stretch_wid=1, stretch_len=1)
    square.shape("square")
    square.color("white")
    square.penup()
    square.setpos(x=-20*i,y=0)
    snack_body.append(square)

screen.mainloop()
