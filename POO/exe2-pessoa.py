class Pessoa:
    def __init__(self, nome, idade=0, peso=0, altura=0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura  

    def envelhecer(self, anos=1):
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)  # Cresce 0.5 cm
            self.idade += 1

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros  

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Peso: {self.peso} kg, Altura: {self.altura} cm")


if __name__ == '__main__':

    pessoa1 = Pessoa("Ana", 15, 55, 160)  # Altura inicial em metros

    pessoa1.mostrar_informacoes()  # Exibe as informações iniciais

    pessoa1.envelhecer(4)  # Ana envelhece 5 anos (e cresce 0,5 cm por ano)
    pessoa1.engordar(3)    # Ana engorda 3 kg
    pessoa1.emagrecer(2)   # Ana emagrece 2 kg

    pessoa1.mostrar_informacoes()  
