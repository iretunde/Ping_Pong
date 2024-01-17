from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.title(('Pong'))
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

# Left Paddle
p1 = Paddle(-350)

screen.onkeypress(p1.move_up, 'q')
screen.onkeypress(p1.move_down, 'a')

# Right Paddle
p2 = Paddle(350)

screen.onkeypress(p2.move_up, 'Up')
screen.onkeypress(p2.move_down, 'Down')

b = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    b.move()

    # Detect collision with the wall
    if b.ycor() >= 290 or b.ycor() <= -290:
        b.bounce_y()

    # Detect collision with paddle
    if (b.distance(p2) < 50 and (335 <= b.xcor() <= 350)) or (b.distance(p1) < 50 and (-350 <= b.xcor() <= -335)):
        b.bounce_x()
        # b.x_move -= 10
        # b.y_move -= 10

    # Detect if P1 paddle misses
    if b.xcor() <= -410:
        for i in range(30):
            b.move()
            screen.update()
        b.goto(0, 0)
        b.bounce_x()
        scoreboard.update_p2_score()

    # Detect if P2 paddle misses
    if b.xcor() >= 410:
        for i in range(30):
            b.move()
            screen.update()
        b.goto(0, 0)
        b.bounce_x()
        scoreboard.update_p1_score()





screen.exitonclick()
