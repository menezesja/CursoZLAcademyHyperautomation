class Prato:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_info(self):
        return f"Prato: {self.nome}, Preço: R${self.preco:.2f}"

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco


class Bebida:
    def __init__(self, nome, preco, tamanho):
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho

    def mostrar_info(self):
        return f"Bebida: {self.nome}, Preço: R${self.preco:.2f}, Tamanho: {self.tamanho}"

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco


class Pedido:
    def __init__(self):
        self.lista_pratos = []
        self.lista_bebidas = []

    def adicionar_prato(self, prato):
        self.lista_pratos.append(prato)

    def adicionar_bebida(self, bebida):
        self.lista_bebidas.append(bebida)

    def remover_prato(self, prato):
        self.lista_pratos.remove(prato)

    def remover_bebida(self, bebida):
        self.lista_bebidas.remove(bebida)

    def calcular_total(self):
        total = sum(prato.preco for prato in self.lista_pratos) + sum(bebida.preco for bebida in self.lista_bebidas)
        return total

    def mostrar_pedido(self):
        itens = [prato.mostrar_info() for prato in self.lista_pratos] + [bebida.mostrar_info() for bebida in self.lista_bebidas]
        total = self.calcular_total()
        return "\n".join(itens) + f"\nTotal do pedido: R${total:.2f}"


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def fazer_pedido(self):
        pedido = Pedido()
        self.pedidos.append(pedido)
        return pedido

    def mostrar_pedidos(self):
        return [f"Pedido {i + 1}:\n{pedido.mostrar_pedido()}" for i, pedido in enumerate(self.pedidos)]


class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.lista_clientes = []
        self.pedidos_finalizados = []

    def adicionar_cliente(self, cliente):
        self.lista_clientes.append(cliente)

    def finalizar_pedido(self, cliente, pedido):
        self.pedidos_finalizados.append(pedido)

    def gerar_relatorio_vendas(self):
        total_vendas = sum(pedido.calcular_total() for pedido in self.pedidos_finalizados)
        return f"Total de vendas: R${total_vendas:.2f}"

    def aplicar_promocao_prato(self, prato, desconto_percentual):
        if 0 <= desconto_percentual <= 100:
            desconto = prato.preco * (desconto_percentual / 100)
            prato.atualizar_preco(prato.preco - desconto)

    def aplicar_promocao_bebida(self, bebida, desconto_percentual):
        if 0 <= desconto_percentual <= 100:
            desconto = bebida.preco * (desconto_percentual / 100)
            bebida.atualizar_preco(bebida.preco - desconto)


# Exemplo de uso
def main():
    restaurante = Restaurante("Delícias do Chef")

    # Adicionando clientes
    cliente1 = Cliente("João")
    restaurante.adicionar_cliente(cliente1)

    # Fazendo pedidos
    pedido1 = cliente1.fazer_pedido()
    
    # Criando pratos e bebidas
    prato1 = Prato("Pizza Margherita", 35.00)
    prato2 = Prato("Lasagna", 40.00)
    bebida1 = Bebida("Coca-Cola", 7.50, "Lata")

    # Adicionando pratos e bebidas ao pedido
    pedido1.adicionar_prato(prato1)
    pedido1.adicionar_prato(prato2)
    pedido1.adicionar_bebida(bebida1)

    # Mostrando pedido
    print(cliente1.mostrar_pedidos()[0])

    # Finalizando pedido
    restaurante.finalizar_pedido(cliente1, pedido1)

    # Gerando relatório de vendas
    print(restaurante.gerar_relatorio_vendas())

    # Aplicando promoção
    print("\nAplicando promoção de 10% no prato 'Pizza Margherita'")
    restaurante.aplicar_promocao_prato(prato1, 10)
    
    # Mostrando pedido atualizado
    print(cliente1.mostrar_pedidos()[0])

    # Gerando relatório de vendas após promoção
    print(restaurante.gerar_relatorio_vendas())


if __name__ == "__main__":
    main()
