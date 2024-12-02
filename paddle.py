
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cordinates, y_cordinates):
        super().__init__()
        self.x_cordinates = x_cordinates
        self.y_cordinates = y_cordinates

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        self.goto(x_cordinates, y_cordinates)



    def up(self):
            new_y = self.ycor() +20
            self.goto(self.xcor(), new_y)

    def down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)




