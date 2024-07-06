from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
import random

# Creating Objects
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
ball = Ball()
turtle = Turtle(shape='square')
scoreboard = Scoreboard()

# Creating paddle both instances
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

def middle_Line():
    """Creates Middle net line"""
    turtle.color('white')
    turtle.penup()
    turtle.goto(0, 300)
    turtle.hideturtle()
    turtle.pensize(3)
    turtle.setheading(270)
    while turtle.ycor() > -320:
        turtle.pendown()
        turtle.forward(20)
        turtle.penup()
        turtle.forward(20)

def multiplayer():
    """Enables Multiplayer key listen"""
    screen.onkeypress(left_paddle.up, 'w')
    screen.onkeypress(left_paddle.down, 's')

def computer_play():
    """Automates left paddle for single player"""
    # Ball is higher than paddle
    left_paddle.disturbance = 30

    left_paddle.SENSITIVITY = random.randint(2, 7)
    if ball.ycor() > left_paddle.ycor() + left_paddle.disturbance:
        left_paddle.up()

    elif ball.ycor() < left_paddle.ycor() + left_paddle.disturbance:
        left_paddle.down()

def game_exit():
    """ End the Game """
    global game_is_on
    game_is_on = False
    scoreboard.game_over()


game_is_on = True
userinput = screen.textinput(title='Choose the mode',
                             prompt="Do you want to play MultiPlayer or SinglePlayer (Type m or s) : ").lower()
# Listening key Presses
screen.listen()
screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')
screen.onkeypress(game_exit, 'e')

if userinput == 'm':
    multiplayer()

speed = 0.05
middle_Line()

# Main game loop
while game_is_on and userinput:
    screen.update()
    time.sleep(ball.ball_speed)

    if userinput == 's':
        computer_play()

    # Ball moving and bouncing
    ball.move()
    ball.bounce(left_paddle, right_paddle)

    # If Left side misses the ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
        ball.bounceX()
        ball.ball_speed = speed

    # If Right Side misses the ball
    elif ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        ball.bounceX()
        ball.ball_speed = speed

screen.exitonclick()
