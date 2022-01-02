# desafio meu pra mim
multiplicador = int(input('Digite um numero para ser feita a tabuada: '))
limite = int(input('Digite um numero para ser o limite: '))
for indice, numero in enumerate(range(multiplicador, multiplicador * limite + 1, multiplicador), 1):
    print(f'{multiplicador} X {indice} = {numero}')
