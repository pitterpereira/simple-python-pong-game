from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        # As tartarugas começam no tamanho 20x20. Estamos criando uma de 100x20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        # Cria o paddle na posição indicada
        self.goto(xcor, ycor)

    def go_up(self):
        # Limita a subida
        if self.ycor() <= 220:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        # Limita a descida
        if self.ycor() >= -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)