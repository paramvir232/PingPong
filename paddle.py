from turtle import Turtle



class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.speed(0)
        self.SENSITIVITY = 20
        self.disturbance = 0

    def up(self):
        """Moves Paddle Upward"""
        if self.ycor() + 50 < 295:
            self.goto(self.xcor(), self.ycor() + self.SENSITIVITY)


    def down(self):
        """Moves Paddle Downward"""
        if self.ycor() - 50 > -295:
            self.goto(self.xcor(), self.ycor() - self.SENSITIVITY)
