from turtle import Turtle
import random

class Food (Turtle):

    def __init__(self, screen, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.penup()
        self._screen = screen
        self.refresh()

    def refresh(self):
        self._x_pos = random.randrange(-(self._screen.screensize()[0] / 2) + 20, (self._screen.screensize()[0] / 2) - 20)
        self._y_pos = random.randrange(-(self._screen.screensize()[1] / 2) + 20, (self._screen.screensize()[1] / 2) - 20)
        self.goto(x=self._x_pos, y=self._y_pos)