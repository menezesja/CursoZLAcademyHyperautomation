''''Crie um algoritmo que exiba a mensagem “número
aceito” se o número digitado pelo usuário for um número
ímpar ou negativo. Caso contrário exiba “número
inválido'''

n = int(input('Informe um numero: '))

if n % 2 != 0 or n < 0:
    print('número aceito')
else:
    print('número inválido')