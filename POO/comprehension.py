# List Comprehension
# 1. Criar uma lista com os quadrados dos números de 0 a 10
quadrados = [x**2 for x in range(11)]
print("Quadrados de 0 a 10:", quadrados)  # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2. Criar uma lista com os números pares de 0 a 10
pares = [x for x in range(11) if x % 2 == 0]
print("Números pares de 0 a 10:", pares)  # Saída: [0, 2, 4, 6, 8, 10]

# Dictionary Comprehension
# 1. Criar um dicionário que mapeia números de 0 a 10 para seus quadrados
quadrados_dict = {x: x**2 for x in range(11)}
print("Dicionário de quadrados:", quadrados_dict)  # Saída: {0: 0, 1: 1, 2: 4, ..., 10: 100}

# 2. Criar um dicionário com apenas os números ímpares de 0 a 10 como chaves e seus cubos como valores
cubos_impares_dict = {x: x**3 for x in range(11) if x % 2 != 0}
print("Dicionário de cubos ímpares:", cubos_impares_dict)  # Saída: {1: 1, 3: 27, 5: 125, 7: 343, 9: 729}

# Set Comprehension
# 1. Criar um conjunto com os quadrados dos números de 0 a 10
quadrados_set = {x**2 for x in range(11)}
print("Conjunto de quadrados:", quadrados_set)  # Saída: {0, 1, 4, 36, 64, 49, 9, 16, 25, 81, 100}

# 2. Criar um conjunto com as vogais em uma frase (sem duplicatas)
frase = "Programação em Python é divertida"
vogais_set = {char for char in frase if char in 'aeiouáéíóúAEIOUÁÉÍÓÚ'}
print("Vogais na frase:", vogais_set)  # Saída: {'o', 'í', 'e', 'a', 'á'}
