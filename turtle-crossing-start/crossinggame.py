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
    
    def run(self):
        self._game_is_on = True
        while self._game_is_on:
            time.sleep(0.1)
            self._screen.update()

    def __del__(self):
        self._screen.mainloop()
