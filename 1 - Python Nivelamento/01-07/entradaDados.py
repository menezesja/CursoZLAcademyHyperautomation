#Entrada de dados

nome = input('Digite seu nome: ')       #todo o resultado é uma string
idade = int(input('Digite sua idade: ') )    #caso seja necessário realizar alguma operação, precisa converter
print('\n')

#Concatenação
print('Olá ' + nome + '!')
print('Sua idade é ' +str(idade))           #só concatena se for string
print('----------------------------------------------------')

#Formatação

print('Olá %s! \nSua idade é %s' %(nome, idade))  #transforma int para string
print('----------------------------------------------------')

#Formatação com str.format()

print('Olá {:s}! \nSua idade é {:d}'.format(nome, idade))  #precisa informar o tipo
print('----------------------------------------------------')

#Formatação com f-string
print(f'olá {nome}!\nSua idade é {idade}')
print('----------------------------------------------------')