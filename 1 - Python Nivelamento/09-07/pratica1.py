'''Crie um programa que imprima a tabuada de
multiplicação de um número N digitado pelo usuário.
Exemplo de entrada: 8
Saída:
1 x 8 = 8
2 x 8 = 16
...
10 x 8 = 80'''

n = int(input("Informe um numero: "))

print(f'\nTabuada de {n}')

for i in range(0, 11):
    resultado = n * i
    print(f'{n} x {i} = {resultado}')