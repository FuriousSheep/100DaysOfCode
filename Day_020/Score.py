from turtle import Turtle, screensize


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#FAFAFA")
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score : {self.score}", align="center",
                   font=("Arial Black", 20))

    def update(self):
        """Changes the score writing to show the updated score"""
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}",
                   align="center", font=("Arial Black", 20))
