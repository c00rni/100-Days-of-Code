from turtle import Turtle
import random

MOVE_DISTANCE = 20

class Ball(Turtle):

    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setheading(random.randrange(360))
    
    def move(self):
        self.fd(MOVE_DISTANCE)

    