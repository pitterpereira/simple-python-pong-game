from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # Começa indo para cima
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move

        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        # Inverte a direção do movimento vertical ao bater na parede
        self.y_move *= -1

    def bounce_x(self):
        # Inverte a direção do movimento horizontal ao bater no paddle
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
