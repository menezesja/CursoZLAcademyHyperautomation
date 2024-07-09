n = int(input("Informe um numero: "))

print(f'\nTabuada de {n}')

for i in range(0, 11):
    resultado = n * i
    print(f'{n} x {i} = {resultado}')