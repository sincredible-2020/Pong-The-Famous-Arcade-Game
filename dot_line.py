from turtle import Turtle


class Dotline(Turtle):

    def __init__(self):
        super().__init__()
        self.pensize(5)
        self.pencolor('white')
        self.hideturtle()
        self.make_line()

    def make_line(self):
        self.up()
        self.goto(0, 300)
        self.right(90)

        while self.ycor() != -300:
            self.down()
            self.forward(15)
            self.up()
            self.forward(15)
