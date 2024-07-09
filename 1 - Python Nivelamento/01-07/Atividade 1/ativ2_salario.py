nome = input('Informe seu nome: ')
salario = float(input('Informe seu salario: '))

salarioAumento = salario * 0.15
salarioAtual = salario + salarioAumento

print('Seu nome é %s\nSalario atual é %s' %(nome, salarioAtual))