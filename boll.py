from turtle import Turtle

class Boll(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.shapesize(stretch_wid=1,stretch_len=1)
        # self.setpos(0, 0)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
