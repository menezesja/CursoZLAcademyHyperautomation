'''Crie um vetor que armazene 10 números digitados pelo
usuário e ao final exiba os números pares digitados.'''

numeros = []

for i in range(10):
    n = int(input(f'Informe um numero, posição {i+1}: '))
    numeros += [n]

print('\nNumeros Pares:')
for n in numeros:
    if n % 2 == 0:
        print(n)