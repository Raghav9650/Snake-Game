from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Sanke Game !!!!!!!")
screen.tracer(0)


snake=Snake()
food=Food()
scores=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segment[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scores.increase()

# detecting wall collision
    if snake.segment[0].xcor()>280 or snake.segment[0].xcor()<(-280) or snake.segment[0].ycor()>280 or snake.segment[0].ycor()<-280 :
        scores.reset()
        snake.reset()
# detecting tail colision
    for segment in snake.segment[1:((len(snake.segment)-1))]:
        if snake.segment[0].distance(segment)<10:
            scores.reset()
            snake.reset()

screen.exitonclick()