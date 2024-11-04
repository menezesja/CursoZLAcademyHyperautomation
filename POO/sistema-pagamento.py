from abc import ABC, abstractmethod

# Classe base Funcionario
class Funcionario(ABC):
    def __init__(self, nome, id_funcionario, salario_base):
        self._nome = nome
        self._id_funcionario = id_funcionario
        self._salario_base = salario_base
        self._bonus = 0

    @abstractmethod
    def calcular_pagamento(self):
        pass

    def adicionar_bonus(self, bonus):
        if bonus < 0:
            raise ValueError("O bônus não pode ser negativo.")
        self._bonus = bonus

    def mostrar_info(self):
        return {
            "Nome": self._nome,
            "ID": self._id_funcionario,
            "Salário Base": self._salario_base
        }


# Subclasse FuncionarioCLT
class FuncionarioCLT(Funcionario):
    def calcular_pagamento(self):
        return self._salario_base + self._bonus


# Subclasse FuncionarioHorista
class FuncionarioHorista(Funcionario):
    def __init__(self, nome, id_funcionario, salario_base, horas_trabalhadas, valor_hora):
        super().__init__(nome, id_funcionario, salario_base)
        if horas_trabalhadas < 0 or valor_hora < 0:
            raise ValueError("Horas trabalhadas e valor da hora não podem ser negativos.")
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora

    def calcular_pagamento(self):
        return (self._horas_trabalhadas * self._valor_hora) + self._bonus


# Subclasse FuncionarioFreelancer
class FuncionarioFreelancer(Funcionario):
    def __init__(self, nome, id_funcionario, salario_base, projetos_concluidos, valor_projeto):
        super().__init__(nome, id_funcionario, salario_base)
        if projetos_concluidos < 0 or valor_projeto < 0:
            raise ValueError("Projetos concluídos e valor do projeto não podem ser negativos.")
        self._projetos_concluidos = projetos_concluidos
        self._valor_projeto = valor_projeto

    def calcular_pagamento(self):
        return (self._projetos_concluidos * self._valor_projeto) + self._bonus


# Classe RelatorioPagamentos
class RelatorioPagamentos:
    def __init__(self):
        self.historico_pagamentos = {}

    def registrar_pagamento(self, funcionario, pagamento):
        if funcionario._id_funcionario not in self.historico_pagamentos:
            self.historico_pagamentos[funcionario._id_funcionario] = []
        self.historico_pagamentos[funcionario._id_funcionario].append(pagamento)

    def gerar_relatorio(self, funcionarios):
        relatorio = []
        for funcionario in funcionarios:
            try:
                pagamento_final = funcionario.calcular_pagamento()
                self.registrar_pagamento(funcionario, pagamento_final)
                info = funcionario.mostrar_info()
                info.update({
                    "Pagamento Final": pagamento_final,
                    "Histórico de Pagamentos": self.historico_pagamentos.get(funcionario._id_funcionario, [])
                })
                relatorio.append(info)
            except Exception as e:
                print(f"Erro ao gerar relatório para {funcionario._nome}: {e}")
        return relatorio


# Função para cadastrar um novo funcionário
def cadastrar_funcionario():
    print("Cadastrar Funcionário")
    nome = input("Nome do funcionário: ")
    id_funcionario = int(input("ID do funcionário: "))
    salario_base = float(input("Salário base do funcionário: "))

    print("\nEscolha o tipo de funcionário:")
    print("1 - CLT")
    print("2 - Horista")
    print("3 - Freelancer")
    tipo = int(input("Digite o número correspondente ao tipo: "))

    if tipo == 1:
        # Funcionário CLT
        funcionario = FuncionarioCLT(nome, id_funcionario, salario_base)
        adicionar_bonus = input("Deseja adicionar um bônus? (s/n): ").lower()
        if adicionar_bonus == 's':
            bonus = float(input("Digite o valor do bônus: "))
            funcionario.adicionar_bonus(bonus)

    elif tipo == 2:
        # Funcionário Horista
        horas_trabalhadas = float(input("Horas trabalhadas no mês: "))
        valor_hora = float(input("Valor por hora: "))
        funcionario = FuncionarioHorista(nome, id_funcionario, salario_base, horas_trabalhadas, valor_hora)

    elif tipo == 3:
        # Funcionário Freelancer
        projetos_concluidos = int(input("Número de projetos concluídos: "))
        valor_projeto = float(input("Valor por projeto: "))
        funcionario = FuncionarioFreelancer(nome, id_funcionario, salario_base, projetos_concluidos, valor_projeto)

    else:
        print("Tipo de funcionário inválido.")
        return None

    return funcionario


# Adicionar funcionários até que o usuário deseje parar
funcionarios = []
while True:
    funcionario = cadastrar_funcionario()
    if funcionario:
        funcionarios.append(funcionario)
    continuar = input("\nDeseja cadastrar outro funcionário? (s/n): ").lower()
    if continuar != 's':
        break

# Geração do relatório
print("\nRelatório de Pagamentos")
relatorio = RelatorioPagamentos()
resultado = relatorio.gerar_relatorio(funcionarios)

# Exibição do relatório
for item in resultado:
    print("\n----------------------------")
    print("Nome:", item["Nome"])
    print("ID:", item["ID"])
    print("Salário Base:", item["Salário Base"])
    print("Pagamento Final:", item["Pagamento Final"])
    print("Histórico de Pagamentos:", item["Histórico de Pagamentos"])
