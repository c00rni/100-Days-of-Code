import colorgram
from turtle import Turtle
import random

class HirstPainting(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.colors = []
        self.screen.setup(width=600, height=800, startx=-270, starty=300)
        self.speed('fastest')
        self.screen.colormode(255)

    def extract_color(self, file_name, nb_color):
        color_list = colorgram.extract(file_name, nb_color)
        for count in range(len(color_list)):
            rgb = color_list[count]
            color = tuple(rgb.rgb)
            self.colors.append(color)

    def paint(self):
        y = 300
        x = -235
        for count in range(100):
            if count % 10 == 0:
                self.penup()
                self.setposition(x , y)
                self.pendown()
                y -= 50
            self.pencolor(random.choice(self.colors))
            self.dot(20)
            self.penup()
            self.forward(50)
            self.pendown()


painting = HirstPainting()
painting.extract_color("images.jpeg", 126)
painting.paint()
painting.screen.mainloop()
