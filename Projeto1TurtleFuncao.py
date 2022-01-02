# codigo feito em aula/codigo professor

from turtle import Turtle
t = Turtle()
t.speed(1)


def obter_distancia():
    resposta = int(
        input("Quantos pixels devemos movimentar para a frente\n"))
    return resposta


def rotacionar_turtle(turtle):
    movimentar_lado = input(
        'Rotacionar para D(direita) E(esquerda) N(não rotacionar) \n')
    if movimentar_lado == 'D':
        rotacionar_direita(turtle)
    elif movimentar_lado == 'E':
        rotacionar_esquerda(turtle)


def rotacionar_direita(turtle):
    angulo = int(input('Quanto para a direita devemos rotacionar? \n'))
    t.right(angulo)


def rotacionar_esquerda(turtle):
    angulo = int(input('Quanto para a esquerda devemos rotacionar? \n'))
    t.left(angulo)


while True:
    FrenteAtras = input('Qual direção deseja ir? F(frente) T(tras)\n')
    if FrenteAtras == 'F':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)

    if FrenteAtras == 'T':
        distancia = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distancia)

    resposta = input('Continuar andando? S/N')
    if resposta not in ('sim', 's', 'S', 'SIM'):
        break
