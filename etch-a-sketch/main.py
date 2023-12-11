from turtle import Turtle

class Sketch(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.screen.setup(600, 600)
        self._distance = 10
        self._angle = 5
        self.screen.onkey(fun=self._forward, key="w")
        self.screen.onkey(fun=self._backward, key="s")
        self.screen.onkey(fun=self._counterClockwise, key="d")
        self.screen.onkey(fun=self._clockwise, key="a")
        self.screen.onkey(fun=self._clearTurtleDrawing, key="c")
        self.screen.listen()
    
    def _forward(self):
        self.fd(self._distance)

    def _backward(self):
        self.backward(self._distance)

    def _counterClockwise(self):
        self.setheading(self.heading() - self._angle)

    def _clockwise(self):
        self.setheading(self.heading() + self._angle)

    def _clearTurtleDrawing(self):
        self.clear()
        self.penup()
        self.home()
        self.pendown()





sketch = Sketch()
sketch.screen.mainloop()
