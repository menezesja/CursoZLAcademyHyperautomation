class Pessoa: 

    def __init__(self, nome, peso, altura, sexo):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def calcular_IMC(self):
        IMC = self.peso / (self.altura ** 2)
        return IMC
    
    def classificacaoIMC(self):
        resultadoIMC = self.calcular_IMC()

        if resultadoIMC < 18.5:
            return 'Abaixo do peso'
        elif 18.5 <= resultadoIMC <= 24.9:
            return 'Peso normal'
        elif 25 <= resultadoIMC <= 29.9:
            return 'Sobrepeso'
        else:
            return 'Obesidade'
        
    def exibir_resultado(self):
        imc = self.calcular_IMC()
        classificacaoIMC = self.classificacaoIMC()
        print(f'Nome: {self.nome}')
        print(f'Sexo: {self.sexo}')
        print(f'IMC: {imc:.2f}')
        print(f'Classificação do IMC: {classificacaoIMC}')
        
nome = input('Digite o nome: ')
sexo = input('Digite o sexo (M/F): ')
peso = float(input('Digite o peso em Kg: '))
altura = float(input('Digite a altura em metros: '))

pessoa = Pessoa(nome, peso, altura, sexo)
pessoa.exibir_resultado()