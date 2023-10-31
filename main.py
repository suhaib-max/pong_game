from turtle import Screen, Turtle
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

#creating while loop to turn animation on
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    boll.move()

    #Dectecting collition with wall

    if boll.ycor() > 280 or boll.ycor() < -280:
        boll.bounce()



screen.exitonclick()
