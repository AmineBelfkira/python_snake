from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import turtle

screen = Screen()
screen.title('Snake Game')


def play():
    screen.clear()
    screen.setup(height=600, width=600)
    screen.bgcolor('black')
    # stop auto-refresh so need to run screen.update()
    screen.tracer(0)
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        # Collision FOOD
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
        
        # Collision SNAKE
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

        # Collision WALL
        if snake.head.xcor() < -300 or snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
            scoreboard.game_over()
            game_is_on = False
    draw_retry_button()


def draw_retry_button():
    button_drawer = turtle.Turtle()
    button_drawer.hideturtle()
    button_drawer.penup()
    button_drawer.goto(-50, -150)
    button_drawer.pendown()

    button_drawer.begin_fill()
    button_drawer.color("White")
    for _ in range(2):
        button_drawer.forward(100)
        button_drawer.right(90)
        button_drawer.forward(75)
        button_drawer.right(90)
    button_drawer.end_fill()

    button_drawer.penup()
    button_drawer.goto(0, -200)
    button_drawer.color("Black")
    button_drawer.write("RETRY", align="center", font=("Arial", 20, "bold"))

    screen.onclick(handle_click)

def handle_click(x, y):
    if -50 < x < 50 and -200 < y < -150:
        play() 

play()
draw_retry_button()
turtle.mainloop()