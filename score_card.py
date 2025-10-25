from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read()) 
        
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scorecard()

    def update_scorecard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./Day1-20/Day20&21/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scorecard()

    def increase_scorecard(self):
        self.score += 1
        self.clear()
        self.update_scorecard()




