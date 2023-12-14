from turtle import Screen
from player import Player

class PongGame:

    def __init__(self) -> None:
        self._screen = Screen()
        self._screen.bgcolor("Black")
        self._screen.tracer(0)
        self._screen.setup(width=1200, height=900)
        self._screen.title("Pong Game")
        self._game_on = False
        self._player1 = Player()
        self._screen.onkey(self._player1.up, "Up")
        self._screen.onkey(self._player1.down, "Down")
        self._screen.listen()

    def launch(self):
        self._game_on = True
        while self._game_on:
            self._screen.update()

    def __del__(self):
        self._screen.mainloop()






        