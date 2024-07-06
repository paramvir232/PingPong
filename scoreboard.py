from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates Score"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 70, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 70, 'normal'))

    def l_point(self):
        """Increment left side score"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increment right side score"""
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays Game over text"""
        self.goto(30, -40)
        if self.l_score < self.r_score:

            self.write(f"GAME OVER\nRight Side Won\U0001F600", align='center', font=('Courier', 40, 'normal'))
        elif self.l_score > self.r_score :

            self.write(f"GAME OVER\nLeft Side Won\U0001F600", align='center', font=('Courier', 40, 'normal'))

        else :
            self.write(f"GAME OVER\nMatch Draw\U0001F600", align='center', font=('Courier', 40, 'normal'))

