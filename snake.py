starting_position=[(0,0),(-20,0),(-40,0)]
from turtle import Turtle
move_distance=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake():
    def __init__(self):
        self.segment=[]
        self.create_snake()

    def create_snake(self):
        for i in starting_position:
           self.add_segment(i)

    def add_segment(self,position):
        segments=Turtle("square")
        segments.color("white")
        segments.penup()
        segments.setposition(position)
        self.segment.append(segments)
    
    def extend(self):
         self.add_segment(self.segment[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg_num-1].xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(move_distance)


    def up(self):
        if self.segment[0].heading()!=DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading()!=UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading()!=RIGHT:
                    self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading()!=LEFT:
                    self.segment[0].setheading(RIGHT)

    def reset(self):
         for segment in self.segment:
              segment.goto(1000000,1000000)
         self.segment.clear()
         self.create_snake()