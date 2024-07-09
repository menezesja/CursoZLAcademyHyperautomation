valorEmprestimo = float(input('Informe o valor do emprestimo: '))
numeroParcelas = int(input('Informe o numero de parcelas: '))
salario = float(input('Informe seu salário: '))

valorParcela = valorEmprestimo / numeroParcelas

if valorParcela <= salario * 0.3:
    print('Emprestimo aprovado')
else:
    print('Emprestimo não aprovado')