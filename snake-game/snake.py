from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        self._snack_body = []
        for i in range(3):
            snake_seg = Turtle()
            snake_seg.shapesize(stretch_wid=1, stretch_len=1)
            snake_seg.shape("square")
            snake_seg.color("white")
            snake_seg.penup()
            snake_seg.goto(x=-MOVE_DISTANCE*i,y=0)
            self._snack_body.append(snake_seg)
        self.head = self._snack_body[0]


    def move(self):
        for seg_num in range(len(self._snack_body) - 1, 0, -1):
            new_x = self._snack_body[seg_num - 1].xcor()
            new_y = self._snack_body[seg_num - 1].ycor()
            self._snack_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
