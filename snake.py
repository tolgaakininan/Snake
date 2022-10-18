from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_snake(self):
        for movement in range(len(self.segments) - 1, 0, -1):
            x_cord = self.segments[movement - 1].xcor()
            y_cord = self.segments[movement - 1].ycor()
            self.segments[movement].goto(x_cord, y_cord)

        self.head.forward(20)

    def add_tail(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.segments[len(self.segments) - 1].xcor(), self.segments[len(self.segments) - 1].ycor())
        self.segments.append(new_segment)

    def up(self):

        self.head.setheading(90)

    def down(self):

        self.head.setheading(270)

    def left(self):

        self.head.setheading(180)

    def right(self):

        self.head.setheading(0)
