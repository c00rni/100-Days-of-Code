from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self._score = 0
        self.penup()
        self.goto(-210,250)
        self.updateScoreBoard()
        self.hideturtle()
        self.speed("fastest")

    def increaseScore(self):
        self._score += 1
        self.setx(-280)
        self.clear()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(f"Level: {self._score}", move=True, align="center", font=FONT)

    def gameOver(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!", move=True, align="center", font=FONT)


