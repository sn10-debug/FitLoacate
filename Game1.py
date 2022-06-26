from turtle import Screen
import time

from Snake import Snake_game
from food import Food
from Score import Score

Screen=Screen()
Screen.setup(width=600,height=600)

Game_over=False
num=0


def starter():
    global Screen,Snake,Foodie,Score1
    Screen.tracer(0)
    Screen.title('Snake Game')
    Screen.bgcolor('black')
    Screen.update()
    Snake=Snake_game(Screen)
    Foodie=Food()
    with open('trial.txt') as file:
        highscore=(file.read())
    Score1=Score(highscore=int(highscore))
    Score1.Score_Changer()
    Snake.take_position()

    Screen.listen()

    Screen.onkey(key='Left',fun=Snake.snake_left)
    Screen.onkey(key='Right',fun=Snake.snake_right)
    Screen.onkey(key='Down',fun=Snake.snake_down)
    Screen.onkey(key='Up',fun=Snake.snake_up)



starter()

while not Game_over:
    Snake.move()
    if abs(Snake.turtles[0].ycor())>=Screen.window_height()/2 or abs(Snake.turtles[0].xcor())>=Screen.window_width()/2:
            
            # Score2=Score(0)
            # Score2.Game_over()
            Score1.score=0
            # Game_over=True
            with open('trial.txt',mode='w') as file:
                file.write(str(Score1.highscore))
            Snake.reset()
            starter()
            

    time.sleep(0.1)
    Screen.update()
    if Snake.turtles[0].distance(Foodie)<15:
        Snake.new_turtle()
        Foodie.Distribute_food()
        Score1.score+=1
        Score1.Score_Changer()
    if Snake.self_collide():
        Score1.score=0
        # Game_over=True
        with open('trial.txt',mode='w') as file:
                file.write(str(Score1.highscore))
        
        Snake.reset()
        starter()
    
            


Screen.mainloop()


