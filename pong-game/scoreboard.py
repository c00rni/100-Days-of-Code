from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self._score1 = 0
        self._score2 = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.updateScoreBoard()
        self.hideturtle()
        self.speed("fastest")

    def increaseScore(self, player):
        if player:
            self._score1 += 1
        else:
            self._score2 += 1
        self.setx(0)
        self.clear()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(f"{self._score1}    {self._score2}", move=True, align="center", font=('Open Sans', 48, 'normal'))

    def gameOver(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!", move=True, align="center", font=('Open Sans', 12, 'normal'))


