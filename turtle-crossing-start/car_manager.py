from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    class Car:
        
        def __init__(self) -> None:
            self._parts = []
            self._color = random.choice(COLORS)

            for n in range(2):
                part = Turtle(shape="square")
                part.penup()
                part.goto(x=20*n, y=0)
                part.color(self._color)
                self._parts.append(part)
            
            self._head = self._parts[0]

        def move(self, speed):
            for part in self._parts:
                part.forward(-speed)
    
    def __init__(self) -> None:
        self._cars = [self.Car()]
        self._speed = STARTING_MOVE_DISTANCE
    
    def move(self):
        for car in self._cars:
            car.move(self._speed)


    