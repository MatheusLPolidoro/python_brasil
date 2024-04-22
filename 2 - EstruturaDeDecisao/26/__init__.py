"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

### Álcool:

- até 20 litros, desconto de 3% por litro
- acima de 20 litros, desconto de 5% por litro
  
### Gasolina:

- até 20 litros, desconto de 4% por litro
- acima de 20 litros, desconto de 6% por litro
 
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o
preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

# Entrada
litros = float(input('Digite o número de litros vendidos: '))
tipo_combustivel = input('Digite o tipo de combustível [A = álcool, G = gasolina]: ').upper()[0]

# Processamento
if tipo_combustivel == 'A':
    preco = 1.9
    if litros > 20:
        desconto = 0.05
    else:
        desconto = 0.03
elif tipo_combustivel == 'G':
    preco = 2.5
    if litros > 20:
        desconto = 0.06
    else:
        desconto = 0.04
else:
    print('Tipo de combustível inválido...')
    exit(1)

valor_pagamento = litros * preco
valor_pagamento = valor_pagamento - valor_pagamento * desconto

# Saída
print(f'Valor a ser pago pelo cliente: {valor_pagamento:.2f}')
