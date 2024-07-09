''''Crie um algoritmo que receba como entrada a idade
digitada pelo usuário, e identifique se ele é um criança,
jovem ou idoso.
criança: até 13 anos
jovem: de 14 a 59 anos
idoso: a partir de 60 anos.'''

idade = int(input('Informe sua idade: '))

if idade < 14:
    print('criança')
elif 14 <= idade <= 59:
    print('jovem')
else:
    print('idoso')