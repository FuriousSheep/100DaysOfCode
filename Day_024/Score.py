from turtle import Turtle, screensize

HIGHSCORE_PATH = "/home/ioannis/Bureau/PythonCourses/Day_024/Highscore.txt"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#FAFAFA")
        self.goto(0, 260)
        self.score = 0
        self.highscore = self.get_highscore()
        self.write(
            f"Score : {self.score}, High Score: {self.highscore}",
            align="center",
            font=("Arial Black", 20)
        )

    def update(self):
        """Changes the score writing to show the updated score"""
        self.score += 1
        print(self.score)
        if self.score > self.highscore:
            self.highscore = self.score
            self.set_highscore()
        self.write_score()

    def reset(self):
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(
            f"Score : {self.score}, High Score: {self.highscore}",
            align="center",
            font=("Arial Black", 20)
        )

    def get_highscore(self):
        with open(HIGHSCORE_PATH) as file:
            highscore = file.read()
        return int(highscore)

    def set_highscore(self):
        with open(HIGHSCORE_PATH, "w") as file:
            file.write(f"{self.score}")
