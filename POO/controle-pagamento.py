from abc import ABC, abstractmethod

# Definindo a classe abstrata Pagamento
class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass
    
    def detalhes_pagamento(self, metodo):
        print(f"Processando pagamento via {metodo}.")

# Subclasse PagamentoCartao que herda de Pagamento
class PagamentoCartao(Pagamento):
    def processar_pagamento(self):
        print("Pagamento processado com cartão.")
        return 'Cartão'

# Subclasse PagamentoBoleto que herda de Pagamento
class PagamentoBoleto(Pagamento):
    def processar_pagamento(self):
        print("Pagamento processado com boleto.")
        return 'Boleto'

# Função para testar os pagamentos
def testar_pagamentos():
    pagamento_cartao = PagamentoCartao()
    pagamento_boleto = PagamentoBoleto()
    
    metodo_cartao = pagamento_cartao.processar_pagamento()
    pagamento_cartao.detalhes_pagamento(metodo_cartao)
    
    metodo_boleto = pagamento_boleto.processar_pagamento()
    pagamento_boleto.detalhes_pagamento(metodo_boleto)

# Executando a função de teste
testar_pagamentos()