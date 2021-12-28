# codigo feito em aula/codigo professor

from turtle import Turtle
t = Turtle()
t.speed(1)
while True:
    FrenteAtras = input('Qual direção deseja ir? F(frente) T(tras)\n')
    if FrenteAtras == 'F':
        distancia = int(
            input("Quantos pixels devemos movimentar para a frente\n"))
        movimentar_lado = input(
            'Rotacionar para D(direita) E(esquerda) N(não rotacionar) \n')
        if movimentar_lado == 'D':
            angulo = int(input('Quanto para a direita devemos rotacionar? \n'))
            t.right(angulo)
        elif movimentar_lado == 'E':
            angulo = int(
                input('Quanto para a esquerda devemos rotacionar? \n'))
            t.left(angulo)
        elif movimentar_lado == 'N':
            print('não movimentar')
        t.forward(distancia)

    if FrenteAtras == 'T':
        distancia = int(
            input("Quantos pixels devemos movimentar para tras? \n"))
        movimentar_lado = input(
            'Rotacionar para para D(direita) E(esquerda) N(não rotacionar) \n')
        if movimentar_lado == 'D':
            angulo = int(input('Quanto para a direita devemos rotacionar? \n'))
            t.right(angulo)
        elif movimentar_lado == 'E':
            angulo = int(
                input('Quanto para a esquerda devemos rotacionar? \n'))
            t.left(angulo)
        elif movimentar_lado == 'N':
            print('não movimentar')
        t.backward(distancia)

    resposta = input('Continuar andando? S/N')
    if resposta not in ('sim', 's', 'S', 'SIM'):
        break
