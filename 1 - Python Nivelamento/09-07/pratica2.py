'''Escreva um programa em Python que receba dois
números inteiros do usuário, inicio e fim, e calcule a soma
de todos os números pares no intervalo fechado entre
esses dois números. O programa deve usar um laço for
para iterar pelo intervalo e somar os números pares. Ao
final, o programa deve exibir a soma.'''

inicio, fim = map(int, input('Informe dois numeros: ').split())

soma = 0

for i in range(inicio, fim):
    if i % 2 == 0:
        soma += i

print(f'A soma dos numeros pares entre {inicio} e {fim} é {soma}')