class Veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @marca.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    
    def informacoes(self):
        print(f'A marca é: {self.marca}')
        print(f'O modelo é: {self.modelo}')

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        Veiculo.__init__(self, marca, modelo)  
        self.__numero_portas = numero_portas

    @property
    def numero_portas(self):
        return self.__numero_portas
    
    @numero_portas.setter
    def numero_portas(self, numero_portas)
        self.__numero_portas = numero_portas
    
    def informacao_completa(self):
        print('Informações do carro')
        self.informacoes()  
        print(f'Número de portas: {self.numero_portas}')
        print('-' * 40)

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, carga):
        Veiculo.__init__(self, marca, modelo)    
        self.__carga = carga

    @property
    def carga(self):
        return self.__carga
    
    def informacao_completa(self):
        print('Informações do carro')
        self.informacoes()  
        print(f'Capacidade da carga: {self.carga} kg')
        print('-' * 40)

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        Veiculo.__init__(self, marca, modelo)   
        self.__cilindrada = cilindrada

    @property
    def cilindrada(self):
        return self.__cilindrada
    
    def informacao_completa(self):
        print('Informações do carro')
        self.informacoes()  
        print(f'Cilindradas: {self.cilindrada} cc')
        print('-' * 40)

carro = Carro('Chevrolet', 'Onix', 4)
carro.informacao_completa()

caminhao = Caminhao('Mercedes-Benz', 'Accelo EURO6', 5.018)
caminhao.informacao_completa()

moto = Moto('Honda', 'CG 160 Start', 162.7)
moto.informacao_completa()