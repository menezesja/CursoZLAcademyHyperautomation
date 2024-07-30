#sets defenidos por {}
#são coleções não ornadenadas, imutavéis  e não indexadas
#pode-se inserir ou remover itens
#não permite duplicação

frutas = {'abacate', 'banana', 'caju', 'banana'}
frutas.add('Kiwi')

animais = {'cachorro', 'gato'}
carros = {'gol', 'uno'}

uniao = frutas | animais | carros

frutas.update(animais)

lista_animais = ['papagaio']
animais.update(lista_animais)

#animais.remove('papagaio')

animais.discard('papagaio')

frutas.pop()

print(frutas)
print(animais)
print(uniao)