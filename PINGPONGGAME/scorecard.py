from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.create_scorecard()

    def create_scorecard(self):
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,200)
        self.color('white')
        self.write(f'SCORE : {self.score}')
    def update(self):
        self.clear()
        self.score+=1
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.color('white')
        self.write(f'SCORE : {self.score}')

    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color('white')
        self.write('GAME OVER')
