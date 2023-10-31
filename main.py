from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

#screen animation offing when  0 give parameter in tracer
screen.tracer(0)

paddal = Turtle()
paddal.shape("square")
#square shape 20 * 20 so 20*5 100
paddal.color("white")
paddal.shapesize(stretch_len=1,stretch_wid=5)
paddal.penup()
paddal.goto(x=350, y=0)





#control

def go_up():
    new_y = paddal.ycor() + 30
    paddal.goto(paddal.xcor(),new_y)

def go_down():
    new_y = paddal.ycor() - 30
    paddal.goto(paddal.xcor(),new_y)

screen.listen()

screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

#creating while loop to turn animation on
game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()
