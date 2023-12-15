from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    class Car:
        
        def __init__(self, y_position) -> None:
            self._parts = []
            self._color = random.choice(COLORS)

            for n in range(2):
                part = Turtle(shape="square")
                part.penup()
                part.goto(x=300+(20*n), y=y_position)
                part.color(self._color)
                self._parts.append(part)
            
            self._head = self._parts[0]

        def move(self, speed):
            for part in self._parts:
                part.forward(-speed)
        
        def clearFromScreen(self):
            for part in self._parts:
                part.clear()
    
    def __init__(self) -> None:
        self._cars = []
        self._speed = STARTING_MOVE_DISTANCE
    
    def move(self):
        car_to_del = 0
        for i in range(len(self._cars)):
            if self._cars[i]._head.xcor() < -340:
                self._cars[i].clearFromScreen()
                car_to_del += 1
            else:
                self._cars[i].move(self._speed)
        self._cars = self._cars[car_to_del:]

    def generate(self):
        if random.randrange(6) == 0:
            car = self.Car(random.randrange(-250,280))
            self._cars.append(car)
    
    def increaseSpeed(self):
        self._speed += MOVE_INCREMENT

    def checkCollision(self, player):
        for car in self._cars:
            if (player.distance(car._parts[0]) < 20) or (player.distance(car._parts[1]) < 20):
                return True
        return False