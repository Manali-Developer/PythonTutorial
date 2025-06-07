from turtle import Turtle

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=360

class Snake:
    """This class have everything related to snake """

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

    def extend(self):
        """Extending the snake once it eats food"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Movements of snake"""
        for seg in range(len(self.segments)-1,0,-1):
            newx=self.segments[seg-1].xcor()
            newy=self.segments[seg-1].ycor()
            self.segments[seg].goto(newx,newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Movements of snake in upwards direction."""
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        """Movements of snake in downwards direction."""
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        """Movements of snake in left direction."""
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Movements of snake in right direction."""
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
