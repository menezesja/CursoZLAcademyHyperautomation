class Veiculo:
    total_veiculos = 0

    def __init__(self, modelo, marca, ano, valor_diario, combustivel):
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__valor_diario = valor_diario
        self.__combustivel = combustivel
        Veiculo.total_veiculos += 1

    # Métodos getter e setter para encapsulamento
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_valor_diario(self):
        return self.__valor_diario

    def set_valor_diario(self, valor_diario):
        self.__valor_diario = valor_diario

    def get_combustivel(self):
        return self.__combustivel

    def set_combustivel(self, combustivel):
        self.__combustivel = combustivel

    def mostrar_informacoes(self):
        return f"Modelo: {self.__modelo}, Marca: {self.__marca}, Ano: {self.__ano}, Combustível: {self.__combustivel}, Valor Diário: R${self.__valor_diario:.2f}"

    def calcular_valor_total(self, dias, desconto=0):
        valor = self.__valor_diario * dias
        if self.__combustivel == 'gasolina':
            valor *= 0.95  # 5% de desconto para gasolina
        if dias > 7:
            valor *= 0.90  # 10% de desconto para mais de 7 dias
        valor -= desconto
        return max(valor, 0)

    @classmethod
    def total_veiculos_cadastrados(cls):
        return cls.total_veiculos

    @classmethod
    def aplicar_aumento(cls, percentual, frota):
        for veiculo in frota:
            novo_valor = veiculo.get_valor_diario() * (1 + percentual / 100)
            veiculo.set_valor_diario(novo_valor)


class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, valor_diario, combustivel, ar_condicionado, cambio):
        super().__init__(modelo, marca, ano, valor_diario, combustivel)
        self.ar_condicionado = ar_condicionado
        self.cambio = cambio

    def calcular_valor_total(self, dias, desconto=0):
        valor = super().calcular_valor_total(dias, desconto)
        if self.cambio == 'automático':
            valor += 50  # Custo adicional para câmbio automático
        if self.ar_condicionado:
            valor += 30  # Custo adicional para ar condicionado
        return max(valor, 0)

    def mostrar_informacoes(self):
        info_basica = super().mostrar_informacoes()
        return f"{info_basica}, Ar Condicionado: {'Sim' if self.ar_condicionado else 'Não'}, Câmbio: {self.cambio}"


class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, valor_diario, combustivel, cilindrada):
        super().__init__(modelo, marca, ano, valor_diario, combustivel)
        self.cilindrada = cilindrada

    def calcular_valor_total(self, dias, desconto=0):
        valor = super().calcular_valor_total(dias, desconto)
        if self.cilindrada > 200:
            valor += 20  # Custo adicional para cilindrada maior que 200cc
        return max(valor, 0)

    def mostrar_informacoes(self):
        info_basica = super().mostrar_informacoes()
        return f"{info_basica}, Cilindrada: {self.cilindrada}cc"

class SistemaAluguel:
    def __init__(self):
        self.frota = []

    def adicionar_veiculo(self, veiculo):
        self.frota.append(veiculo)

    def mostrar_frota(self):
        for veiculo in self.frota:
            print(veiculo.mostrar_informacoes())

    def calcular_valor_total_aluguel(self, veiculo, dias, desconto=0):
        return veiculo.calcular_valor_total(dias, desconto)

def menu():
    sistema = SistemaAluguel()

    while True:
        print("\nMenu do Sistema de Aluguel de Veículos")
        print("1. Adicionar Carro")
        print("2. Adicionar Moto")
        print("3. Mostrar Frota")
        print("4. Calcular Valor do Aluguel")
        print("5. Aplicar Aumento no Valor Diário de Todos os Veículos")
        print("6. Mostrar Total de Veículos Cadastrados")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            modelo = input("Digite o modelo do carro: ")
            marca = input("Digite a marca do carro: ")
            ano = int(input("Digite o ano do carro: "))
            valor_diario = float(input("Digite o valor diário de aluguel: "))
            combustivel = input("Digite o tipo de combustível (gasolina/flex): ").lower()
            ar_condicionado = input("Possui ar condicionado? (s/n): ").lower() == 's'
            cambio = input("Digite o tipo de câmbio (manual/automático): ").lower()

            carro = Carro(modelo, marca, ano, valor_diario, combustivel, ar_condicionado, cambio)
            sistema.adicionar_veiculo(carro)
            print("Carro adicionado com sucesso!")

        elif opcao == '2':
            modelo = input("Digite o modelo da moto: ")
            marca = input("Digite a marca da moto: ")
            ano = int(input("Digite o ano da moto: "))
            valor_diario = float(input("Digite o valor diário de aluguel: "))
            combustivel = input("Digite o tipo de combustível (gasolina/flex): ").lower()
            cilindrada = int(input("Digite a cilindrada da moto: "))

            moto = Moto(modelo, marca, ano, valor_diario, combustivel, cilindrada)
            sistema.adicionar_veiculo(moto)
            print("Moto adicionada com sucesso!")

        elif opcao == '3':
            sistema.mostrar_frota()

        elif opcao == '4':
            sistema.mostrar_frota()
            index = int(input("Digite o índice do veículo para calcular o aluguel (começando do 0): "))
            dias = int(input("Digite o número de dias do aluguel: "))
            desconto = float(input("Digite o valor do desconto (se houver): "))

            if 0 <= index < len(sistema.frota):
                veiculo = sistema.frota[index]
                valor_aluguel = sistema.calcular_valor_total_aluguel(veiculo, dias, desconto)
                print(f"Valor total do aluguel: R${valor_aluguel:.2f}")
            else:
                print("Índice de veículo inválido.")

        elif opcao == '5':
            percentual = float(input("Digite o percentual de aumento no valor diário (%): "))
            sistema.aplicar_aumento(percentual, sistema.frota)
            print(f"Aumento de {percentual}% aplicado com sucesso a todos os veículos!")

        elif opcao == '6':
            print(f"Total de veículos cadastrados: {Veiculo.total_veiculos_cadastrados()}")

        elif opcao == '0':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida, tente novamente.")


# Executar o menu
menu()