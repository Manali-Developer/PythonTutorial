from turtle import Turtle
import time

"""Imported all related modules n classes"""

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=360

"""Constants"""

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creating snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        """Adding new segments"""
        newsegment=Turtle("square")
        newsegment.color("white")
        newsegment.penup()
        newsegment.goto(position)
        self.segments.append(newsegment)

    """Extending the snake once it eats food"""

    def extend(self):
        self.add_segment(self.segments[-1].position())

    """Movements of snake"""

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            newx=self.segments[seg-1].xcor()
            newy=self.segments[seg-1].ycor()
            self.segments[seg].goto(newx,newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
