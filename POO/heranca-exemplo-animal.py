class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f'{self.nome} está fazendo som')

class Cachorro(Animal):
    def fazer_som(self):
        print(f'{self.nome} está latindo.')

class Gato(Animal):
    def fazer_som(self):
        print(f'{self.nome} está miando.')


a = Animal('Animal Genérico')
a.fazer_som()

c = Cachorro('Rex')
c.fazer_som()

g = Gato('Mingau')
g.fazer_som()