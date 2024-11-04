palavras = ['Python', 'map', 'lambda', 'exemplo', 'função', 'filter']

palavras_grandes = list(filter(lambda palavra: len(palavra) > 5, palavras))

print(palavras_grandes)