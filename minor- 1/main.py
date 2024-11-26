from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("My snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

# setting keys to give commands

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collosion with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collosion with food

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        score.reset()
        snake.reset()
    #detect collosion with wall

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            score.reset()
            snake.reset()



screen.exitonclick()