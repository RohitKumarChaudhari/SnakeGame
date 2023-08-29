from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def clear_score(self):
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
