numero = int(input('Informe um número inteiro: '))

if numero == 0:
    print('numero neutro')
elif (numero % 2) == 0:
    print('numero par')
else:
    print('numero impar')