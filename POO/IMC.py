class Pessoa: 

    def __init__(self, nome, peso, altura, sexo):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def calcular_IMC(self):

        IMC = self.peso / (self.altura * self.altura)

        print(f'Nome: {self.nome}\nSexo: {self.sexo}\nFaixa de peso: {IMC}')


pessoa1 = Pessoa('Alice', 56, 1.54, 'F')
pessoa2 = Pessoa('Pedro', 80, 1.90, 'M')


pessoa1.calcular_IMC()
pessoa2.calcular_IMC()