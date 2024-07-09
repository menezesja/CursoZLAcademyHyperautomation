inicio, fim = map(int, input('Informe dois numeros: ').split())

soma = 0

for i in range(inicio, fim):
    if i % 2 == 0:
        soma += i

print(f'A soma dos numeros pares entre {inicio} e {fim} é {soma}')