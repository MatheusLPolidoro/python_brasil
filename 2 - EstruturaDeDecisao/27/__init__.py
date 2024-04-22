"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

|               |       Até 5 Kg|           Acima de 5 Kg|
|---------------|---------------|------------------------|
|Morango        | R$ 2,50 por Kg|          R$ 2,20 por Kg|
|Maçã           | R$ 1,80 por Kg|          R$ 1,50 por Kg|

Se o cliente comprar mais de 8 Kg em frutas ou o valor
total da compra ultrapassar R$ 25,00, receberá ainda um
desconto de 10% sobre este total.

Escreva um algoritmo para:
ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

# Entrada
kg_morangos = float(input('Digite a quantidade de morangos (em Kg): '))
kg_macas = float(input('Digite a quantidade de maças (em Kg): '))

# Processamento
if kg_morangos > 5:
    preco_morango = 2.2
elif kg_morangos > 0:
    preco_morango = 2.5
else:
    print('Quantidade de morangos inválida...')
    exit(1)

if kg_macas > 5:
    preco_macas = 1.5
elif kg_macas > 0:
    preco_macas = 1.8
else:
    print('Quantidade de maças inválida...')
    exit(1)

valor_pagamento = preco_morango * kg_morangos + preco_macas * kg_macas

if kg_morangos + kg_macas > 8 or valor_pagamento > 25:
    valor_pagamento = valor_pagamento * 0.9

# Saída
print(f'Valor total a ser pago: {valor_pagamento:.2f}')
