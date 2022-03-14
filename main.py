from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

sleep_time = 0.05

# Gera o objeto do tipo tela
screen = Screen()

# Desenha uma linha no meio da tela
linha = Turtle()
linha.color("white")
linha.goto(0, 400)
linha.goto(0, -400)

# Configurações do objeto do tipo tela
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Desliga a atualização automática da tela, permitindo o uso dos updates manuais
screen.tracer(0)

# Analisa as entradas de botões
screen.listen()

# Informa o estado do jogo
game_is_on = True

# Criação dos objetos do tipo paddle
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Escuta os botões definidos para movimentar os paddles
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Cria o objeto do tipo bola
ball = Ball()

scoreboard = Scoreboard()

# Enquanto o jogo estiver acontecendo...
while game_is_on:
    # Seta um tempo antes de executar
    time.sleep(sleep_time)
    # Atualiza o estado da tela
    screen.update()
    # Move a bola
    ball.move()

    # Detectando colisões com a parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Inverte a direção
        ball.bounce_y()

    # Detecta as colisões com o paddle direito
    # Se a distância do centro do paddle for menor que 50 e a bola tiver passado de 320 horizontalmente...
    if ball.distance(right_paddle) < 53 and ball.xcor() > 320 and ball.x_move > 0 \
        or ball.distance(left_paddle) < 53 and ball.xcor() < -320 and ball.x_move < 0 :
        
        # Inverte a direção da bola
        ball.bounce_x()
        sleep_time *= 0.9

    # Detectar quando a bola passa do paddle direito
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        sleep_time = 0.05

    # Detectar quando a bola passa do paddle esquerdo
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        sleep_time = 0.05

# Evita que a tela se feche após a execução. Ela se fechará com um clique
screen.exitonclick()