from turtle import Screen
from player import Player
from ball import Ball
import time

class PongGame:

    def __init__(self) -> None:
        self._screen = Screen()
        self._screen.bgcolor("Black")
        self._screen.tracer(0)
        self._screen.setup(width=1200, height=800)
        self._screen.title("Pong Game")
        self._game_on = False
        self._player1 = Player(-550)
        self._screen.onkey(self._player1.up, "Up")
        self._screen.onkey(self._player1.down, "Down")
        self._player2 = Player(550)
        self._screen.onkey(self._player2.up, "w")
        self._screen.onkey(self._player2.down, "s")
        self._ball = Ball()
        self._screen.listen()

    def launch(self):
        self._game_on = True
        while self._game_on:
            self._collision()
            self._ball.move()
            self._screen.update()
            time.sleep(0.1)
    
    def _collision(self):
        yBallPos = self._ball.position()[1]
        xBallPos = self._ball.position()[0]
        for block in self._player1.getPaddle() + self._player2.getPaddle():
            if block.distance(self._ball) < 20:
                self._ball.x_move *= -1
        if yBallPos > 380 or yBallPos < -380:
            self._ball.y_move *= -1
        if xBallPos > 550 or xBallPos < -550:
            self._game_on = False
        
    def __del__(self):
        self._screen.mainloop()






        