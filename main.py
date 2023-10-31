from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")



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




screen.exitonclick()
