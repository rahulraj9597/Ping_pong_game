from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard

my_screen = Screen()
my_screen.bgcolor('black')
my_screen.setup(width=800,height=600)
my_screen.tracer(0)
my_screen.title('PINGPONG GAME')

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
score = Scorecard()

while True:
    my_screen.update()
    time.sleep(0.1)
    my_screen.listen()
    my_screen.onkey(fun=right_paddle.move_up,key='Up')
    my_screen.onkey(fun=right_paddle.move_down,key='Down')
    my_screen.onkey(fun=left_paddle.move_up,key='w')
    my_screen.onkey(fun=left_paddle.move_down,key='s')
    ball.move_ball()
    if ball.ycor() > 200 or ball.ycor() < -200:
        ball.bounce_ball_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_ball_x()
        score.update()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_ball_x()
        score.update()
    if ball.xcor() > 400 or ball.xcor() < -400:
        score.game_over()








my_screen.exitonclick()