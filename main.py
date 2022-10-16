from turtle import Turtle, Screen
from paddle import PaddleUser
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


net = Turtle()
net.hideturtle()
net.color("white")
net.penup()
net.goto(0, 300)

l_paddle = PaddleUser((-350, 0))
r_paddle = PaddleUser((350, 0))
theball = Ball()
scoreboard = ScoreBoard()


for _ in range(19):
    net.pensize(6)
    net.setheading(270)
    net.forward(15)
    net.penup()
    net.forward(15)
    net.pendown()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(theball.move_speed)
    screen.update()
    theball.move()
    #detect the collision with the wall
    if theball.ycor() > 280 or theball.ycor() < -280:
        theball.bounce_y()
    #detect collision with the paddle
    if theball.distance(r_paddle) < 50 and theball.xcor() > 320 or theball.distance(
            l_paddle) < 50 and theball.xcor() < -320:
        theball.bounce_x()
    #detect R paddle misses
    if theball.xcor() > 380:
        theball.restart_position()
        scoreboard.l_point()
    # detect L paddle misses
    if theball.xcor() < -380:
        theball.restart_position()
        scoreboard.r_point()

screen.exitonclick()

