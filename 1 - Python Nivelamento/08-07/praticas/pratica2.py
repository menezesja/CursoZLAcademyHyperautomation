while True:
    n = int(input('Escolha uma opção\n1 - Sacar\n2 - Depositar\n3 - Sair\nOpção: '))
    match n:
        case 1:
            print('Operação bem sucedida\n')
        case 2:
            print('Operação bem sucedida\n')
        case 3:
            print('Encerrado!\n')
            break
        case _:
            print('Opção Inválida\n')