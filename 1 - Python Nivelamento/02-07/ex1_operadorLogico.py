'''Crie um algoritmo que receba como entrada a nota e a
frequência de um aluno. O aluno estará aprovado se a
nota for maior ou igual a 7.5 e a frequência maior ou igual
a 75. Caso contrário ele estará reprovado.'''

nota = float(input('Informe a nota do aluno: '))
frequencia = int(input('Informe a frequência do aluno: '))

if nota >= 7.5 and frequencia >= 75:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')