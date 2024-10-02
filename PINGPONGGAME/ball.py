from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10

    def create_ball(self):
        self.shape('circle')
        self.color('white')
        self.goto(0,0)

    def move_ball(self):
        self.penup()
        new_x_ball = self.xcor() + self.x_move
        new_y_ball = self.ycor() + self.y_move
        self.goto(new_x_ball,new_y_ball)

    def bounce_ball_y(self):
        self.y_move *= -1
    def bounce_ball_x(self):
        self.x_move *= -1



