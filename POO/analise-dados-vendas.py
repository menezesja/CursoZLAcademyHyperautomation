from functools import reduce

# Lista de vendas
vendas = [
    {'produto': 'Laptop', 'quantidade': 2, 'preco_unitario': 3000, 'regiao': 'Norte'},
    {'produto': 'Mouse', 'quantidade': 10, 'preco_unitario': 50, 'regiao': 'Sul'},
    {'produto': 'Teclado', 'quantidade': 5, 'preco_unitario': 150, 'regiao': 'Norte'},
    {'produto': 'Monitor', 'quantidade': 3, 'preco_unitario': 700, 'regiao': 'Leste'},
    {'produto': 'Cadeira', 'quantidade': 4, 'preco_unitario': 500, 'regiao': 'Oeste'},
    {'produto': 'Laptop', 'quantidade': 1, 'preco_unitario': 3000, 'regiao': 'Sul'},
    {'produto': 'Mouse', 'quantidade': 15, 'preco_unitario': 45, 'regiao': 'Norte'},
    {'produto': 'Monitor', 'quantidade': 2, 'preco_unitario': 750, 'regiao': 'Sul'},
    {'produto': 'Cadeira', 'quantidade': 7, 'preco_unitario': 450, 'regiao': 'Norte'}
]

# 1. Calcular o Total de Vendas por Produto

# Usando map() para calcular o total de cada venda
totais_vendas = list(map(lambda venda: venda['quantidade'] * venda['preco_unitario'], vendas))
print("Totais de cada venda:", totais_vendas)

# Usando reduce() para somar todos os totais de vendas
total_geral_vendas = reduce(lambda x, y: x + y, totais_vendas)
print("Total geral de vendas:", total_geral_vendas)

# 2. Filtrar Vendas de Alto Valor

# Filtrar registros onde o total de vendas é maior que R$ 2000
vendas_alto_valor = list(filter(lambda venda: venda['quantidade'] * venda['preco_unitario'] > 2000, vendas))
print("Vendas de alto valor:", vendas_alto_valor)

# 3. Calcular a Receita Total por Região

def receita_por_regiao(vendas, regiao):
    # Filtra as vendas para a região especificada
    vendas_regiao = filter(lambda venda: venda['regiao'] == regiao, vendas)
    # Calcula o total de vendas para a região
    totais_regiao = map(lambda venda: venda['quantidade'] * venda['preco_unitario'], vendas_regiao)
    # Usa reduce para somar o total da região
    receita_total = reduce(lambda x, y: x + y, totais_regiao, 0)
    return receita_total

# Calcula a receita total para cada região
receita_norte = receita_por_regiao(vendas, 'Norte')
receita_sul = receita_por_regiao(vendas, 'Sul')
receita_leste = receita_por_regiao(vendas, 'Leste')
receita_oeste = receita_por_regiao(vendas, 'Oeste')

print("Receita total por região:")
print(f"Norte: R${receita_norte:.2f}")
print(f"Sul: R${receita_sul:.2f}")
print(f"Leste: R${receita_leste:.2f}")
print(f"Oeste: R${receita_oeste:.2f}")
