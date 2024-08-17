from turtle import Turtle
import random
RANGE_POSITION = 280
COLOR = 'Blue'
SHAPE = 'circle'
SPEED = 'fastest'

class Food(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(COLOR)
        self.speed(SPEED)
        
        self.position_x = random.randint(-RANGE_POSITION,RANGE_POSITION)
        self.position_y = random.randint(-RANGE_POSITION,RANGE_POSITION)
        self.goto(self.position_x, self.position_y)
    
    def refresh(self):
        old_position_x = self.position_x
        old_position_y = self.position_y
        while (old_position_x == self.position_x and old_position_y == self.position_y):
            self.position_x = random.randint(-RANGE_POSITION,RANGE_POSITION)
            self.position_y = random.randint(-RANGE_POSITION,RANGE_POSITION)
        self.goto(self.position_x, self.position_y)