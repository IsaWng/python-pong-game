import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
# Turn off the trace to avoid the visual movement of the paddle initialization
screen.tracer(0)

left_paddle = Paddle((-390, 0))
right_paddle = Paddle((380, 0))

ball = Ball()
scoreboard = ScoreBoard()

# Listen to the key
screen.listen()
# The function parameter move_up,move_down should NOT be with ()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    # refresh the screen as the trace being turned off before
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect collision to the head and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # right paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_x()

    # left paddle collision
    if ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    # detect collision to the right wall, left scored
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.write_score()
    # detect collision to the left wall, right scored
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.write_score()

screen.exitonclick()
