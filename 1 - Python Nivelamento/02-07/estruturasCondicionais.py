valorA, valorB = map(int, (input('Informe o valor de A e B, separado por um espaço: ').split())) #função map, mapeia para a lista de variaveis que esta esperando a entrada

if valorA > valorB:
    print(f'A maior que B, valor de A: {valorA}')
else:
    print(f'B maior que A, valor de B: {valorB}')