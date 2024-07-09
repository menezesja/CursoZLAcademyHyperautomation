#artigo 1
nome = input('Informe o nome do artigo 1: ')
preco = float(input('Informe o preço do artigo 1: '))
desconto = float(input('Informe o desconto do artigo 1: '))

descontoArtigo1 = (preco * (desconto/100))
valorArtigo1 = preco - descontoArtigo1
print('----------------------------------------------------')

#artigo 2
nome2 = input('Informe o nome do artigo 2: ')
preco2 = float(input('Informe o preço do artigo 2: '))
desconto2 = float(input('Informe o desconto do artigo 2: '))

descontoArtigo2 = (preco2 * (desconto/100))
valorArtigo2 = preco2 - descontoArtigo2
print('----------------------------------------------------')

#artigo 3
nome3 = input('Informe o nome do artigo 3: ')
preco3 = float(input('Informe o preço do artigo 3: '))
desconto3 = float(input('Informe o desconto do artigo 3: '))

descontoArtigo3 = (preco3 * (desconto/100))
valorArtigo3 = preco3 - descontoArtigo3
print('----------------------------------------------------')

valorFinal = valorArtigo1 + valorArtigo2 + valorArtigo3

print('Artigo 1 - %s\nValor com desconto aplicado - %s\n' %(nome, valorArtigo1))
print('Artigo 2 - %s\nValor com desconto aplicado - %s\n' %(nome, valorArtigo2))
print('Artigo 3 - %s\nValor com desconto aplicado - %s\n' %(nome, valorArtigo3))

print('O valor final é %s', valorFinal)

