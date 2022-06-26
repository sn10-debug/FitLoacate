# from _typeshed import Self


import turtle

# from Score import Score


class Snake_game:
    
    
    
    def __init__(self,screen):
        self.Screen=screen
        self.turtles=[]
        
        


    def take_position(self):
        from turtle import Turtle
  
        for i in range(3):
            turtle_ex1=Turtle('square')
            turtle_ex1.color('white')
            turtle_ex1.penup()
            turtle_ex1.forward(-20*(i))
            self.turtles.append(turtle_ex1)
        self.information={i:(self.turtles[i].xcor(),self.turtles[i].ycor()) for i in range(len(self.turtles))}
    

    def move(self):
        
        self.turtles[0].forward(20)
        for i in range(1,len(self.turtles)):
            self.turtles[i].goto(self.information[i-1])
        for i in range(len(self.turtles)):
            self.information[i]=(self.turtles[i].xcor(),self.turtles[i].ycor())
        # print((self.turtles[0].xcor(),self.turtles[0].ycor()))
        
        
        
        
    def snake_up(self):
        if not int(self.turtles[0].heading())==270:
            self.turtles[0].setheading(90)
        # self.turtles[0].left(90)
    def snake_right(self):
        if not int(self.turtles[0].heading())==180:
            self.turtles[0].setheading(0)
        # self.turtles[0].right(90)
        self.Screen.update()
    def snake_down(self):
        if not int(self.turtles[0].heading())==90:
            self.turtles[0].setheading(270)
        # self.turtles[0].right(90)
        
        
    def snake_left(self):
        if not int(self.turtles[0].heading())==0:
            self.turtles[0].setheading(180)
        # self.turtles[0].left(180)
        self.Screen.update()
    
    def new_turtle(self):
        Turtle_new=turtle.Turtle('square')
        Turtle_new.color('white')
        Turtle_new.penup()
        self.turtles.append(Turtle_new)
        self.information[len(self.turtles)-1]=(Turtle_new.xcor(),Turtle_new.ycor())

    def self_collide(self):
        num=0
        head=self.turtles[0]
        for i in self.turtles[1:]:
            if head.distance(i)<1:
                num+=1
                break
        if num>0:
            
            # from Score import Score
            # over=Score()
            # over.Game_over()
            return True
        else:
            return False
    def reset(self):
        self.Screen.clearscreen()
        self.turtles=[]
        # self.take_position()




