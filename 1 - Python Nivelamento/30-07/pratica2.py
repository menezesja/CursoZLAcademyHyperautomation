'''Crie um programa capaz de criar uma matriz quadrada
(n x n) e que calcule e exiba:
● a soma dos elementos da diagonal principal
● a soma dos elementos da diagonal secundária.
● a soma dos elementos da diagonal principal com a
secundária.'''

def criar_matriz(n):
    matriz= []
    for i in range(n):
        linha = []
        for j in range(n):
            elemento = int(input(f'Digite o elemento [{i}][{j}] da matriz: '))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

def soma_diagonal_secundaria(matriz):
    soma = 0
    n = len(matriz)
    for i in range(n):
        soma += matriz[i][n - i -1]
    return soma


def main():
    n = int(input('Informe o tamanho da matriz quadrada (nxn): '))
    matriz = criar_matriz(n)

    soma_principal = soma_diagonal_principal(matriz)
    soma_secundaria = soma_diagonal_secundaria(matriz)
    soma_total = soma_principal + soma_secundaria

    print(f'Soma da diagonal principal: {soma_principal}')
    print(f'Soma da diagonal secundária: {soma_secundaria}')
    print(f'Soma da diagonal principal e secundária: {soma_total}')

if __name__ == '__main__':
    main()    