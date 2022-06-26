from turtle import Turtle

class Scorer(Turtle):
    def __init__(self):
        super().__init__()
        
    def updater(self,score):
        
        self.reset()
        self.color('black')
        self.penup()
        self.goto(-600,280)
        self.pendown()
        self.write(f'Level:{score}',False,'center',font=('Arial',20,'normal'))
        self.penup()
        self.color('white')
    
    def over(self):
        display=Turtle()

        display.write('GAME OVER',False,'center',font=('Arial',20,'normal'))
        display.color('white')