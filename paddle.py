from turtle import Screen, Turtle


class Paddle(Turtle):
    def __init__(self,coords):
       
        super().__init__()
        self.shape('square')
        self.shapesize(3,0.5,1)
        self.color('white')
        self.penup()
        self.goto(coords,0)
        


    def upward(self):
        self.setheading(90)
        self.forward(20)
        self.setheading(0)
    
    def downward(self):
        self.setheading(270)
        self.forward(20)
        self.setheading(0)
    


        
            

        


    