n = int(input('Informe um numero: '))

#inicializa os dois primeiros numeros da sequência
a, b = 1, 1

#imprime os dois primeiros numeros
if n >= 1:
    print(f'{a}', end='')
if n >= 2:
    print(f', {b}', end='')

#gera sequência fibonacci
for i in range(2, n):
    a, b = b, a + b
    print(f', {b}', end='')
    