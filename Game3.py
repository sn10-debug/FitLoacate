from turtle import Screen
from Player import Player
from Cars import Processor
from Score_board_3 import Scorer
import time
Screen=Screen()
Screen.setup(width=600,height=600)
Screen.tracer(0)
        
Racer=Player(coords=(0,-280))
Proceesor1=Processor(Racer)
score_board=Scorer()
score_board.updater(Racer.level)
Screen.update()
def up():
    if not Game_over:
        Racer.up()
        
        if Racer.ycor()>=280:
            Racer.start()
            Racer.level+=1
            Proceesor1.speed+=5
            score_board.updater(Racer.level)
        Screen.update()    

Screen.listen()
Screen.onkey(key='Up',fun=up)


Game_over=False

while not Game_over:
    Proceesor1.gen_cars()
    time.sleep(0.1)
    Screen.update()
    Proceesor1.move_cars()
    if Proceesor1.checker():
        score_board.over()
        Game_over=True
    

Screen.exitonclick()