# desafio meu pra mim
multiplicador = int(input('Digite um numero para ser feita a tabuada: '))
limite = int(input('Digite um numero para ser o limite: '))
for indice, numero in enumerate(range(multiplicador, multiplicador * limite + 1, multiplicador), 1): # A ordem é especificamente onde deve começar, quantos devem ter de limite, quantidade de 'pulos'. Vulgo 'start,stop,step'
    print(f'{multiplicador} X {indice} = {numero}')
