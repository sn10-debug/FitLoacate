from turtle import Turtle
import random
from Score import Score
from ScoreBoard_2 import Scorer

class Ball(Turtle):
    def __init__(self,Player1,Player2):
        super().__init__(shape='circle')
        self.color('white')
        self.setheading(random.randint(20,30))
        self.Player1=Player1
        self.Player2=Player2
        self.Active='Player1'
        self.penup()
        self.score1=0
        self.score2=0
        self.Score_board1=Scorer((100,300))
        self.Score_board2=Scorer((-100,300))
        self.Score_board1.updater(self.score1)
        self.Score_board2.updater(self.score2)

    def move(self):
        
        if self.distance(self.Player1)<35:
            self.setheading(random.randint(195,250))
            self.Active='Player2'
            print('Collided Player1')
        elif  self.distance(self.Player1.xcor()+40,self.ycor())<10:
            self.setheading(random.randint(195,250))
            self.Active='Player2'
            self.score2+=1
            self.Score_board2.updater(self.score2)

        elif self.distance(self.xcor(),-340)<10:
            
            if self.Active=='Player1':
                self.setheading(random.randint(20,45))
                

            else:
                self.setheading(random.randint(135,160))
        
        elif self.distance(self.xcor(),340)<10:
            if self.Active=='Player1':
                self.setheading(random.randint(295,300))
            else:
                self.setheading(random.randint(225,250))
                
        elif self.distance(self.Player2)<35:
            self.setheading(random.randint(290,315))
            self.Active='Player1'
            print('Collided Player2')
        elif self.distance(self.Player2.xcor()-40,self.ycor())<10 :

            self.setheading(random.randint(290,315))
            self.Active='Player1'
            self.score1+=1
            self.Score_board1.updater(self.score1)


        self.forward(20)




    
