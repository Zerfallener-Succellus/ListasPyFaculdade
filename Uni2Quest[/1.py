def calcular_totais_produtos(produtos):
    totais = {}

    for produto in produtos:
        nome = produto['nome']
        valor = produto['valor']
        quantidade = produto['quantidade']

        custo_total = valor  * quantidade

        if nome in totais:
            totais[nome] += custo_total
        else:
            totais[nome] = custo_total

    return totais

produtos = [
    {'nome': 'Feijão', 'valor': 5.3, 'quantidade': 3},
    {'nome': 'Arroz', 'valor': 4.2, 'quantidade': 2},
    {'nome': 'Feijão', 'valor': 5.3, 'quantidade': 1},
    {'nome': 'Macarrão', 'valor': 3.8, 'quantidade': 4}
]

# Calculando os totais
totais = calcular_totais_produtos(produtos)

# Exibindo os resultados
for produto, total in totais.items():
    print(f"{produto}: R${total:.2f}")