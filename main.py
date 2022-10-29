import turtle
import time
import keyboard

from dot_line import Dotline
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


wn = turtle.Screen()
wn.setup(width=900, height=600)
wn.bgcolor('black')
wn.tracer(0)


alex = Dotline()
paddle1 = Paddle()
paddle1.goto(420, 0)
paddle2 = Paddle()
paddle2.goto(-420, 0)

ball = Ball()
scoreboard = Scoreboard()



wn.listen()
wn.onkeypress(lambda: paddle1.upwards(), 'Up')
wn.onkeypress(lambda: paddle1.downwards(), 'Down')
wn.onkeypress(lambda: paddle2.upwards(), 'w')
wn.onkeypress(lambda: paddle2.downwards(), 's')


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    ball.movement()
    wn.update()

    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 or ball.distance(paddle2) < 50:
        ball.bounce_x()

    if ball.xcor() > 440:
        ball.reset_position()
        scoreboard.l_score_update()

    if ball.xcor() < -440:
        ball.reset_position()
        scoreboard.r_score_update()

wn.exitonclick()
