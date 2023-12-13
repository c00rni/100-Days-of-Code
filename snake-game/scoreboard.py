from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, score=0, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self._score = score
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.updateScoreBoard()
        self.hideturtle()
        self.speed("fastest")

    def increaseScore(self):
        self._score += 1
        self.setx(0)
        self.clear()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(f"Score = {self._score}", move=True, align="center", font=('Open Sans', 12, 'normal'))


