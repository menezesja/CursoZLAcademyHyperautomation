'''Crie um vetor que armazene 10 números digitados pelo
usuário e ao final exiba os números pares digitados.'''

numeros = []
pares = []

for i in range(10):
    n = int(input(f'Informe um numero, posição {i+1}: '))
    numeros.append(n)

for n in numeros:
    if n % 2 == 0:
        pares.append(n)       
        
if pares:
    print(f'\nNumeros pares: {pares}\n')
else:
    print('\nNão há numeros pares!')