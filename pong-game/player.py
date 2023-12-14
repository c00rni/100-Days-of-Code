from turtle import Turtle

MOVE_DISTANCE = 20

class Player:

    def __init__(self, x_position, paddle_lenght=4) -> None:
        self._paddle = []

        for i in range(paddle_lenght):
            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.speed("fastest")
            block.goto(x=x_position, y=MOVE_DISTANCE*i)
            self._paddle.append(block)

    def up(self):
        for block in self._paddle:
            block.setheading(90)
            block.forward(MOVE_DISTANCE)

    def down(self):
        for block in self._paddle:
            block.setheading(270)
            block.forward(MOVE_DISTANCE)
    
    def getPaddle(self):
        return self._paddle
