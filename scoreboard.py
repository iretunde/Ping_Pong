from turtle import Turtle

FONT = ('Arial', 35, 'normal')
ALIGN = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.p1_score = 0
        self.p2_score = 0
        self.write_p1_score()
        self.write_p2_score()
        self.board_divider()


    def board_divider(self):
        # self.pendown()
        # self.goto(0, 200)
        for i in range(-250, 270, 20):
            self.goto(0, i )
            self.write('|',False, 'center', 'Calibri')
        # self.penup()

    def write_p1_score(self):
        self.goto(-125, 225)
        self.write(self.p1_score,False, ALIGN, FONT)

    def write_p2_score(self):
        self.goto(125, 225)
        self.write(self.p2_score,False, ALIGN, FONT)

    def update_p1_score(self):
        self.clear()
        self.p1_score += 1
        self.write_p1_score()
        self.write_p2_score()
        self.board_divider()

    def update_p2_score(self):
        self.clear()
        self.p2_score += 1
        self.write_p1_score()
        self.write_p2_score()
        self.board_divider()