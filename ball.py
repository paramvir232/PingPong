from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.continue_bounce_trace = 0
        self.clear()
        self.ball_speed = 0.05

    def move(self):
        """Moves ball in a line"""
        randomx = self.xcor() + self.x_move
        randomy = self.ycor() + self.y_move
        self.goto(randomx, randomy)

    def bounceX(self):
        """Reverses X-coordinates"""
        self.x_move *= -1

    def bounce(self, lpaddle, rpaddle):
        """Bounce the ball with given both paddle"""
        ldistance = self.distance(lpaddle)
        rdistance = self.distance(rpaddle)

        # Bounce From walls
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

        # Bounce From Paddle
        if (rdistance < 50 and (380 > self.xcor() > 320)) or (ldistance < 50) and (
                -380 < self.xcor() < -320):
            if self.continue_bounce_trace == 0:
                self.ball_speed *= 0.9
                self.bounceX()

            self.continue_bounce_trace += 1
        else:
            self.continue_bounce_trace = 0

    def reset_position(self):
        """Reset ball position to origin"""
        self.goto(0, 0)

