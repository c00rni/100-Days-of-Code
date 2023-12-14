from turtle import Turtle

class Player:

    def __init__(self, paddle_lenght=4) -> None:
        self.paddle = []

        for i in range(paddle_lenght):
            block = Turtle(shape="square")
            block.color("white")
            block.penup()
            block.goto(x=0, y=20*i)
            self.paddle.append(block)