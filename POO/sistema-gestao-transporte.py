from abc import ABC, abstractmethod

# Classe abstrata Veiculo
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, custo_km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.custo_km = custo_km

    @abstractmethod
    def calcular_custo_viagem(self, distancia):
        pass
    
    @abstractmethod
    def obter_informacoes(self):
        pass

# Subclasse Caminhao
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, custo_km, capacidade_carga, custo_extra_por_tonelada):
        super().__init__(marca, modelo, ano, custo_km)
        self.capacidade_carga = capacidade_carga
        self.custo_extra_por_tonelada = custo_extra_por_tonelada

    def calcular_custo_viagem(self, distancia):
        return distancia * self.custo_km + (self.capacidade_carga * self.custo_extra_por_tonelada)

    def obter_informacoes(self):
        return (f"Caminhão {self.marca} {self.modelo}, Ano: {self.ano}, Capacidade de carga: {self.capacidade_carga}t")

# Subclasse Onibus
class Onibus(Veiculo):
    def __init__(self, marca, modelo, ano, custo_km, capacidade_passageiros, tarifa_por_passageiro):
        super().__init__(marca, modelo, ano, custo_km)
        self.capacidade_passageiros = capacidade_passageiros
        self.tarifa_por_passageiro = tarifa_por_passageiro

    def calcular_custo_viagem(self, distancia):
        return distancia * self.custo_km + (self.capacidade_passageiros * self.tarifa_por_passageiro)

    def obter_informacoes(self):
        return (f"Ônibus {self.marca} {self.modelo}, Ano: {self.ano}, Capacidade de passageiros: {self.capacidade_passageiros}")

# Subclasse VeiculoPassageiro
class VeiculoPassageiro(Veiculo):
    def __init__(self, marca, modelo, ano, custo_km, tipo_veiculo, capacidade_passageiros):
        super().__init__(marca, modelo, ano, custo_km)
        self.tipo_veiculo = tipo_veiculo
        self.capacidade_passageiros = capacidade_passageiros

    def calcular_custo_viagem(self, distancia):
        return distancia * self.custo_km

    def obter_informacoes(self):
        return (f"{self.tipo_veiculo} {self.marca} {self.modelo}, Ano: {self.ano}, Capacidade de passageiros: {self.capacidade_passageiros}")

# Classe GestaoFrota
class GestaoFrota:
    def __init__(self):
        self.frota = []

    def adicionar_veiculo(self, veiculo):
        self.frota.append(veiculo)

    def mostrar_frota(self):
        for veiculo in self.frota:
            print(veiculo.obter_informacoes())

    def calcular_custo_total(self, distancia):
        custo_total = sum(veiculo.calcular_custo_viagem(distancia) for veiculo in self.frota)
        return custo_total

# Exemplo de uso:
caminhao = Caminhao("Volvo", "FH", 2020, 2.5, 10, 1.2)
onibus = Onibus("Mercedes", "Sprinter", 2019, 1.8, 30, 0.5)
carro = VeiculoPassageiro("Ford", "Focus", 2021, 0.9, "Carro", 5)

frota = GestaoFrota()
frota.adicionar_veiculo(caminhao)
frota.adicionar_veiculo(onibus)
frota.adicionar_veiculo(carro)

frota.mostrar_frota()
print("Custo total para 100 km:", frota.calcular_custo_total(100))
