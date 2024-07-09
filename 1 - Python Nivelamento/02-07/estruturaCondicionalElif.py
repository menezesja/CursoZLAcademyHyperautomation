valorA, valorB = map(int, (input('Informe o valor de A e B, separado por um espaço: ').split())) #função map, mapeia para a lista de variaveis que esta esperando a entrada

if valorA > valorB:
    print(f'A maior que B\nValor de A: {valorA} \nValor de B:{valorB}')
elif valorA < valorB:
    print(f'B maior que A\nValor de A: {valorA} \nValor de B:{valorB}')
else:
    print('Os valores de A e B são iguais!')