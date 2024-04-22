"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:


|               |       Até 5 Kg|           Acima de 5 Kg|
|---------------|---------------|------------------------|
|File Duplo     | R$ 4,90 por Kg|          R$ 5,80 por Kg|
|Alcatra        | R$ 5,90 por Kg|          R$ 6,80 por Kg|
|Picanha        | R$ 6,90 por Kg|          R$ 7,80 por Kg|

Para atender a todos os clientes, cada cliente poderá levar apenas
um dos tipos de carne da promoção, porém não há limites para a quantidade
de carne por cliente. Se compra for feita no cartão Tabajara o cliente
receberá ainda um desconto de 5% sobre o total da compra.

Escreva um programa que peça o tipo e a quantidade de carne comprada 
pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, 
valor do desconto e valor a pagar.
"""

# Entrada
tipo_carne = int(
    input(
        'Tipos de carnes'
        +'\n\t1 - File Duplo'
        +'\n\t2 - Alcatra'
        +'\n\t3 - Picanha'
        +'\nDigite um número para selecionar o tipo de carne: '
    )
)
kg_carne = float(input('Quandos kg: '))
cartao_tabajara = input(
    'Deseja pagar com o cartão Tabajara [S/N]: '
).upper()[0] == 'S'

# Processamento
if tipo_carne == 1:
    tipo_carne_str = 'File Duplo'
    preco_1 = 4.9
    preco_2 = 5.8
elif tipo_carne == 2:
    tipo_carne_str = 'Alcatra'
    preco_1 = 5.9
    preco_2 = 6.8
elif tipo_carne == 3:
    tipo_carne_str = 'Picanha'
    preco_1 = 6.9
    preco_2 = 7.8
else:
    print('Tipo de carne inválida...')
    exit(1)

valor_total = valor_pagamento = kg_carne * preco_2

if kg_carne > 5:
    valor_pagamento = valor_total
    valor_desconto = 0
elif kg_carne > 0:
    valor_pagamento = kg_carne * preco_1
    valor_desconto = valor_total - valor_pagamento
else:
    print('Quantidade de carne invalida...')
    exit(1)

if cartao_tabajara:
    tipo_pagamento = 'Cartão Tabajara'
    valor_desconto += valor_pagamento * 0.05
    valor_pagamento = valor_pagamento * 0.95
else:
    tipo_pagamento = 'Sem cartão Tabajara'


# Saída
print(f'{"-" * 50}\n{"CUPOM FISCAL":^50}\n{"-" * 50}')
print(f'{"Tipo de carne:":.<25}{tipo_carne_str:.>25}')
print(f'{"Quantidade de carne:":.<25}{kg_carne:.>25}')
print(f'{"Preço total:":.<25}{valor_total:.>25}')
print(f'{"Tipo de pagamento:":.<25}{tipo_pagamento:.>25}')
print(f'{"Valor do desconto:":.<25}{valor_desconto:.>25}')
print(f'{"Valor a pagar:":.<25}{valor_pagamento:.>25}')
