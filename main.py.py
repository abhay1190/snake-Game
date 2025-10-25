from turtle import Screen, time
from snake import Snake
from food import Food
from score_card import ScoreCard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = ScoreCard()


# key binding
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

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorecard.increase_scorecard()
    
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        # scorecard.game_over()
        scorecard.reset()
        snake.reset()

    # Detect collision with tail

    # Using the loop and if condistion

    # If the head collides with any segment in the tail trigger game_over
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scorecard.game_over()


    # Using SLICING METHOD  to get rid of 2 conditions
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scorecard.reset()
            snake.reset()
            # game_is_on = False
            # scorecard.game_over()
            




    








screen.exitonclick()
