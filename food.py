from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.Distribute_food()

        self.shapesize(0.5,0.5,1)
      
    
    def Distribute_food(self):
        import random
        self.goto(random.randint(-280,280),random.randint(-240,240))


    