from functools import reduce

numeros = [1, 2, 3, 4, 5]

soma = reduce(lambda x, y: x + y, numeros)

print(soma)