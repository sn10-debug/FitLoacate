from turtle import Turtle

class Scorer(Turtle):
    def __init__(self,coords):
        super().__init__()
        self.coords=coords
        
        

    def updater(self,score):
        self.reset()
        self.color('white')
        self.penup()
        self.goto(self.coords)
        self.pendown()
        self.write(f'Score : {score}',False,'center',font=('Arial',20,'normal'))
        self.color('black')
    
    def winner(self,player):
        self.reset()
        self.color('white')
        self.penup()
        self.goto(self.coords)
        self.pendown()
        self.write('{player} is the winner',False,'center',font=('Arial',20,'normal'))

