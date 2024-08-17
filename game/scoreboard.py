from turtle import Turtle

COLOR = 'White'
FONT = ("Arial", 24, "normal")
ALIGN = "center"
class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()
        
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
        