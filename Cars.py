from turtle import Turtle
import random
colours=['violet','indigo','blue','green','yellow','orange','red']
class Car(Turtle):
    def __init__(self,racer):
        super().__init__('square')
        self.color(random.choice(colours))
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.goto(300,random.randint(-250,250))
        self.setheading(180)
        self.racer=racer
    def collide(self):
        if self.distance(self.racer)<20:
            return True
        else:
            return False


class Processor():
    def __init__(self,racer):
        self.cars=[]
        self.speed=10
        self.racer=racer
    
    def gen_cars(self):
        num=random.randint(1,6)
        if num==3 or num==5:
            car_el=Car(self.racer)
            self.cars.append(car_el)

    def move_cars(self):
        for i in self.cars:
            i.forward(self.speed)
            
        for i in self.cars:
            if i.xcor()<-800:
                self.cars.remove(i)
    def checker(self):
        bool=[]
        for i in self.cars:
            bool.append(f'{i.collide()}')
        if 'True' in bool:
            return True
        else:
            return False

            