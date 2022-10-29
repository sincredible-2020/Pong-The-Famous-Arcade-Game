from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.up()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=4.5)
        self.left(90)

    def upwards(self):
        if self.ycor() < 250:
            self.forward(20)

    def downwards(self):
        if self.ycor() > -250:
            self.backward(20)
