from turtle import Screen
from food import Food
from snake import Snake
import time
import turtle
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
turtle.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.clear()
        score.update_score()
        food.refresh()
        snake.extend()

    # Detect collision with Wall
    if snake.head.xcor() > 270 or snake.head.ycor() > 270 or snake.head.ycor() < -270 or snake.head.xcor() < -270:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            time.sleep(1)
            score.game_over()
            game_is_on = False

screen.exitonclick()
