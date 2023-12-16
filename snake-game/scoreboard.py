from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, score=0, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self._score = score
        with open("score.txt", "r") as scrore_file:
            self._high_score = int(scrore_file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.updateScoreBoard()
        self.hideturtle()
        self.speed("fastest")

    def increaseScore(self):
        self._score += 1
        if self._score > self._high_score:
            self._high_score = self._score
            with open("score.txt", "w") as scrore_file:
                scrore_file.write(str(self._high_score))
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.setx(0)
        self.clear()
        self.write(f"Score = {self._score}, Highiest score = {self._high_score}", move=True, align="center", font=('Open Sans', 12, 'normal'))

    def gameReset(self):
        self._score = 0
        self.updateScoreBoard()



