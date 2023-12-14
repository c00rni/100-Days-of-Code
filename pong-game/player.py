from turtle import Turtle

MOVE_DISTANCE = 20

class Player:

    def __init__(self, paddle_lenght=4) -> None:
        self.paddle = []

        for i in range(paddle_lenght):
            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.speed("fastest")
            block.goto(x=0, y=MOVE_DISTANCE*i)
            self.paddle.append(block)

    def move(self):
        pass

    def up(self):
        for block in self.paddle:
            block.setheading(90)
            block.forward(MOVE_DISTANCE)

    def down(self):
        for block in self.paddle:
            block.setheading(270)
            block.forward(MOVE_DISTANCE)
