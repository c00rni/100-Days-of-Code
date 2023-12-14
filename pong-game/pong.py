from turtle import Screen

class PongGame:

    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.bgcolor("Black")
        self.screen.setup(width=1200, height=900)
        self.screen.title("Pong Game")

    def __del__(self):
        self.screen.mainloop()






        