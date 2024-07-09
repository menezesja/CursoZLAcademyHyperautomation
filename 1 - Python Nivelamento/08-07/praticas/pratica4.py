quantidadeNota = 0
somaNota = 0

while True:
    n = float(input('Informe a nota do aluno: '))
    
    if 0 <= n <= 10:
        somaNota += n
        quantidadeNota += 1

    elif n < 0:
        media = somaNota/quantidadeNota
        print(f'A média é: {media:.2f}')  
        break

    else:
        print('Nota fora do intervalo de 0 e 10!')