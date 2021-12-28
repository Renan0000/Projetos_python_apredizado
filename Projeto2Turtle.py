# Meu codigo/solução

from turtle import Turtle
t = Turtle()
t.speed(1)
print('Seja bem-vindo \n Para iniciar digite S para fechar digite N')
inicio_fim = input('')

if inicio_fim == 'n':
    print('Adeus')
    exit()

while inicio_fim == 's':

    FrenteAtras = input(
        'Qual direção deseja ir? F(frente) B(atras) N(não deseja se mover) \n')

    if FrenteAtras == 'F':
        distancia = int(input("Quantos pixels deseja movimentar? \n"))
        angulo = input(
            'Qual angulo/graus deseja se mover? D(direita) E(esquerda) N(não deseja se mover) \n')
        if angulo == 'D':
            grau = int(input("Quantos graus deseja virar? \n"))
            t.right(grau)
            t.forward(distancia)
        elif angulo == 'E':
            grau = int(input("Quantos graus deseja virar? \n"))
            t.left(grau)
            t.forward(distancia)
        elif angulo == 'N':
            t.forward(distancia)

        resposta = input("Deseja continuar?")
        if resposta not in ('sim', 's', 'Sim', 'SIM'):
            break

    if FrenteAtras == 'B':
        distancia = int(input("Quantos pixels deseja movimentar? \n"))
        angulo = input(
            'Qual angulo/graus deseja se mover? D(direita) E(esquerda) N(não deseja se mover) \n')
        if angulo == 'D':
            grau = int(input("Quantos graus deseja virar? \n"))
            t.right(grau)
            t.backward(distancia)
        elif angulo == 'E':
            grau = int(input("Quantos graus deseja virar? \n"))
            t.left(grau)
            t.backward(distancia)
        elif angulo == 'N':
            t.backward(distancia)

        resposta = input("Deseja continuar?")
        if resposta not in ('sim', 's', 'Sim', 'SIM'):
            break
