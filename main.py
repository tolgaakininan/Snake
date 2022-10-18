from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

skor = 0
starting_position = [(0, 0), (-20, 0), (-40, 0)]
ekran = Screen()
ekran.setup(800, 800)
ekran.bgcolor("black")
ekran.title("KEVIN DURANT")
ekran.tracer(0)
game_is_on = True
yilan = Snake()
yemek = Food()
ekran.listen()
skor = Scoreboard()

while game_is_on:
    ekran.onkey(yilan.up, "Up")
    ekran.onkey(yilan.down, "Down")
    ekran.onkey(yilan.left, "Left")
    ekran.onkey(yilan.right, "Right")
    ekran.update()
    time.sleep(0.05)
    yilan.move_snake()
    if yilan.head.distance(yemek) < 15:
        yemek.refresh()
        yilan.add_tail()
        skor.increase_score()
  if yilan.head.xcor() > 380 or yilan.head.xcor() < -380 or yilan.head.ycor() > 380 or yilan.head.ycor() < -380:

        skor.reset()
        yilan.snake_reset()
    for piksel in yilan.segments[1:]:

        if yilan.head.distance(piksel) < 10:

            skor.reset()
            yilan.snake_reset()
ekran.exitonclick()
