a, b = map(float, (input('Informe o valor de A e B: ').split()))

op = int(input('Escolha uma opção:\n1 - Exibir a soma\n2 - Exibir a subtração\n3 - Exibir a multiplicação\n4 - Exibir a divisão\nOpção: '))

match op:
    case 1:
        resultado = a + b
        print(f'O resultado da soma de A e B é {resultado}')
    
    case 2:
        resultado = a - b
        print(f'O resultado da subtração de A e B é {resultado}')
    
    case 3:
        resultado = a * b
        print(f'O resultado da multiplicação de A e B é {resultado}')
    
    case 4:
        resultado = a / b
        print(f'O resultado da divisão de A e B é {resultado}')
    
    case _:
        print(f'Opção inválida')