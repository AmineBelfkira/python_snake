from turtle import Turtle
import os

COLOR = 'White'
FONT = ("Arial", 24, "normal")
ALIGN = "center"
HIGH_SCORE_FILE = "high_score.txt"
class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.hight_score = self.get_highest_score()
        self.show_score()

    def show_score(self):
        self.write(f"Score = {self.score} | Highest Score = {self.hight_score}", align=ALIGN, font=FONT)
     
    def get_highest_score(self):
        if os.path.isfile(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, 'r') as f:
                line = f.read().strip()
        try:
            return int(line)
        except ValueError:
            return 0
        
    def new_highest_score(self, new_score):
        self.hight_score = new_score
        with open(HIGH_SCORE_FILE, 'r') as f:
            f.write(str(new_score))
           
    def increase_score(self):
        self.score += 1
        if self.score > self.hight_score:
            self.new_highest_score(self.score)
        self.clear()
        self.show_score()
        
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
        
        