salario = float(input('Informe seu salario: '))
tempo = int(input('Informe seu tempo de trabalho: '))

if tempo >= 5:
    bonus = salario * 0.20
    print(f'Bônus a receber {bonus}')
else:
    bonus = salario * 0.10
    print(f'Bônus a receber {bonus}')