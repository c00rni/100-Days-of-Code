from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, game, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.setheading(90)
        self.resetStart()
        self._game = game

    def move(self):
        self.fd(MOVE_DISTANCE)
        self.hasFinished()

    def hasFinished(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.resetStart()
            self._game.increaseLevel()

    def resetStart(self):
        self.setpos(STARTING_POSITION)


    
