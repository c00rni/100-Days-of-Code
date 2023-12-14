from turtle import Turtle
from math import pi
import random

MOVE_DISTANCE = 20

class Ball(Turtle):

    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = random.randrange(20)
        self.y_move = random.randrange(20)
    
    def move(self):
        self.setposition(self.xcor() + self.x_move, self.ycor() + self.y_move)
    
    #def invertAngle(self):
    #   self.setheading(180 - self.heading())

    