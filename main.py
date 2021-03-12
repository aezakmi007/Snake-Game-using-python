import time
from turtle import  Screen
from snake import Snake
from food import Food
from  score import Score


screen = Screen();
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
sc = Score()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down,  'Down')
screen.onkey(snake.right,  'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collision with food
    if snake.segments[0].distance(food) < 15:
         print("Collided")
         food.refresh()
         snake.extend()
         sc.increase_score()

    #Detect Collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            sc.reset()
            snake.reset()

    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        sc.reset()
        snake.reset()


















screen.exitonclick()