from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coordinates):
        super().__init__()
        self.create_paddle()
        self.goto(coordinates)

    def create_paddle(self):
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y_coordinate = self.ycor()+20
        self.goto(self.xcor(),new_y_coordinate)

    def move_down(self):
        new_y_coordinate = self.ycor() - 10
        self.goto(self.xcor(), new_y_coordinate)
