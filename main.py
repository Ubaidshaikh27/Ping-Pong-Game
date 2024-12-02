from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")


screen.tracer(0)



r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()


screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")
scoreboard = Scoreboard()


Game_is_on = True

while Game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or  ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()



    if ball.xcor() >380:
        ball.reset()
        scoreboard.r_point()



    if ball.xcor() < - 380:
        ball.reset()
        scoreboard.l_point()




screen.exitonclick()
