import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

class CrossingGame:

    def __init__(self) -> None:
        self._screen = Screen()  
        self._screen.setup(width=600, height=600)
        self._screen.tracer(0)
        self._screen.title("Crossing Turtle Game")
        self._player = Player(game=self)
        self._screen.onkey(self._player.move, "Up")
        self._screen.listen()
        self._car_manager = CarManager()
        self._scoreboard = Scoreboard()
    
    def run(self):
        self._game_is_on = True
        while self._game_is_on:
            time.sleep(0.1)
            self._checkCollision()
            self._screen.update()
            self._car_manager.move()
            self._car_manager.generate()
            time.sleep(0.1)
        self._screen.mainloop()

    def increaseLevel(self):
        self._car_manager.increaseSpeed()
        self._scoreboard.increaseScore()

    def _checkCollision(self):
        if self._car_manager.checkCollision(self._player):
            self._game_is_on = False
            self._scoreboard.gameOver()
