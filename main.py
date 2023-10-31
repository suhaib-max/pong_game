from turtle import Screen, Turtle
from score_board import Score_board
import paddel
from paddel import Paddle
from boll import Boll
import time
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

#screen animation offing when  0 give parameter in tracer
screen.tracer(0)

r_paddel = Paddle((350, 0))
l_paddel = Paddle((-350, 0))
#control

screen.listen()

screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")

#
screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")

boll = Boll()
score_board = Score_board()

#creating while loop to turn animation on
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(boll.move_speed)
    boll.move()

    #Dectecting collition with wall

    if boll.ycor() > 280 or boll.ycor() < -280:
        boll.bounce_y()

    #Detecting collition with boll
    if boll.distance(r_paddel) < 50 and boll.xcor() > 320 or boll.distance(l_paddel) < 50 and boll.xcor() < -320 :
         boll.bounce_x()

    # Detect right paddel (paddel go from 340 to 360)
    if boll.xcor() > 380:
        boll.reset_position()
        score_board.l_point()

    # Detect left paddel (paddel go from 340 to 360)
    if boll.xcor() < -380:
        boll.reset_position()
        score_board.r_point()


screen.exitonclick()
