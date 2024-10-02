from PIL.ImageChops import screen

from paddle import Paddle
from turtle import Screen
from ball import Ball

my_screen = Screen()
my_screen.bgcolor('black')

p1 = Paddle((-300,300))
b = Ball()
my_screen.listen()
my_screen.onkey(p1.move_up,'w')

my_screen.exitonclick()