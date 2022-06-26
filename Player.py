from turtle import Turtle

MOVE_DISTANCE=10
class Player(Turtle):
    def __init__(self,coords):
        super().__init__('turtle')
        self.penup()
        self.goto(coords)
        self.coords=coords
        self.setheading(90)
        self.level=0

    def up(self):
        self.forward(MOVE_DISTANCE)

    def start(self):
        self.goto(self.coords)