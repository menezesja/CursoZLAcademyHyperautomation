from datetime import datetime

class Cliente:
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

class Conta:
    def __init__(self, numero, saldo=0):
        self.__numero = numero
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # Métodos para realizar operações
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        else:
            return "Saldo insuficiente."

    def depositar(self, valor):
        self.__saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso."

    def transferir(self, valor, conta_destino):
        if valor <= self.__saldo:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            return f"Transferência de R${valor:.2f} realizada com sucesso para a conta {conta_destino.numero}."
        else:
            return "Saldo insuficiente para a transferência."

    def mostrar_saldo(self):
        return f"Saldo atual: R${self.__saldo:.2f}"


class Movimentacao:
    def __init__(self, id, cliente, conta):
        self.id = id  
        self.data_hora = datetime.now()  
        self.cliente = cliente 
        self.conta = conta  

    # Método para realizar a operação
    def operacao(self, tipo, valor=0, conta_destino=None):
        if tipo == "sacar":
            resultado = self.conta.sacar(valor)
        elif tipo == "depositar":
            resultado = self.conta.depositar(valor)
        elif tipo == "transferir" and conta_destino:
            resultado = self.conta.transferir(valor, conta_destino)
        elif tipo == "mostrar saldo":
            resultado = self.conta.mostrar_saldo()
        else:
            resultado = "Operação inválida."

        # Registro da operação
        self.log_operacao(tipo, valor)
        return resultado

    # Método para logar a operação
    def log_operacao(self, tipo, valor):
        print(f"Movimentação ID: {self.id} \nOperação: {tipo.capitalize()} \nValor: R${valor:.2f} \nData e Hora: {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')} \nCliente: {self.cliente.nome} \nConta: {self.conta.numero}\n")
        print('-'*110)

cliente1 = Cliente("12345678900", "João Silva")
cliente2 = Cliente("98765432100", "Maria Souza")

conta1 = Conta("001", 1000)
conta2 = Conta("002", 500)

movimentacao1 = Movimentacao(1, cliente1, conta1)  # Movimentação com ID 1
movimentacao2 = Movimentacao(2, cliente2, conta2)  # Movimentação com ID 2

print(movimentacao1.operacao("mostrar saldo"))
print(movimentacao1.operacao("sacar", 200))
print(movimentacao1.operacao("mostrar saldo"))

print(movimentacao2.operacao("depositar", 300))
print(movimentacao2.operacao("transferir", 100, conta1))
print(movimentacao2.operacao("mostrar saldo"))
print(movimentacao1.operacao("mostrar saldo"))