from turtle import Turtle,Screen
from paddle import Paddle


Screen=Screen()
Screen.setup(600,600)
Screen.bgcolor('black')
Screen.listen()
Screen.tracer(0)
from ball import Ball
liner=Turtle()
liner.goto(0,-320)
liner.color('white')
liner.pensize(9)
liner.setheading(90)
for i in range(32):
    if i%2==0:
        liner.pendown()
        liner.forward(20)
    else:
        liner.penup()
        liner.forward(20)


Screen.update()
# print(Screen.window_width())
Player1=Paddle(Screen.window_width())
Player2=Paddle(-(Screen.window_width()))
ball_play=Ball(Player1=Player1,Player2=Player2)
ball_play.speed(0)
Game_over=False
Player1.speed(0)
Player2.speed(0)
def up1():
    Player1.upward()
    Screen.update()
def down1():
    Player1.downward()
    Screen.update()

def down2():
    Player2.downward()
    Screen.update()
def up2():
    Player2.upward()
    Screen.update()


Screen.onkey(key='Up', fun=up1)
Screen.onkey(key='Down', fun=down1)
Screen.onkey(key='u', fun=up2)
Screen.onkey(key='d', fun=down2)
Screen.update()
import time


while not Game_over:
    ball_play.move()
    time.sleep(0.1)
    Screen.update()
    if ball_play.score1==21:
        Game_over=True
        ball_play.Score_board1.winner('Right')
    if ball_play.score2==21:
        Game_over=True
        ball_play.Score_board2.winner('Right')
    




Screen.exitonclick()