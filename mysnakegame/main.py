from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

LEVELOFDIFFICULTY={1:0.4,2:0.3,3:0.1}
TIME=0.1


if __name__ == '__main__':
    """Screen setup"""
    screen=Screen() #screen object created.
    screen.bgcolor("black")
    screen.setup(width=500,height=500)
    screen.title("Snake Game")

    """Object creations for all classes"""

    snake=Snake()
    food=Food()
    scoreboard=Scoreboard()

    """selection of level of difficulty by user"""
    scoreboard.difficulty()

    """Movement control of snake with arrow keys"""
    screen.tracer(0)
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

    """Starting the game"""
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(LEVELOFDIFFICULTY.get(scoreboard.User_choice,TIME))#setting the speed accorfing to difficulty
        snake.move()
        """detect collision with food"""
        if snake.head.distance(food)<15:
            print("snake collided to food")
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        """detect collision with wall"""
        if snake.head.xcor()>240 or snake.head.xcor()<-240 or snake.head.ycor()>240 or snake.head.ycor()<-240:
            print("head collided")
            scoreboard.gameover()
            game_is_on=False

        """detect collision with tail"""
        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                game_is_on=False
                scoreboard.gameover()   
    screen.exitonclick()
