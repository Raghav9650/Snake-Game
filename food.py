from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color('blue')
        random_x=random.randint(-278,278)
        random_y=random.randint(-278,278)
        self.goto(random_x,random_y)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x=random.randint(-277,277)
        random_y=random.randint(-277,277)
        self.goto(random_x,random_y)
       