'''Crie um vetor que armazene 10 números digitados pelo
usuário e ao final exiba os números pares digitados.'''

numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input(f'Informe um numero, posição {i+1}: '))

print('\nNumeros Pares:')
for n in numeros:
    if n % 2 == 0:
        print(n)