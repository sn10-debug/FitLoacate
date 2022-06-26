from turtle import Turtle

class Score(Turtle):
    def __init__(self,highscore):
        global Screen
        super().__init__()
        self.score=0
        self.highscore=highscore
        # self.Score_Changer()
         

    def Score_Changer(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.reset()
        self.penup()
        self.goto((0,250))
        self.pendown()
        self.color('white')
        self.write(f'Score : {self.score} Highscore : {self.highscore}',False,'center',font=('Arial',20,'normal'))
        self.color('black')
    
    def Game_over(self):
        self.penup()
        self.goto((0,-250))
        self.pendown()
        self.color('white')
        self.write(f'Game Over.',False,'center',font=('Arial',20,'normal'))
        self.color('black')
    
        



# Score1=Score()





        


