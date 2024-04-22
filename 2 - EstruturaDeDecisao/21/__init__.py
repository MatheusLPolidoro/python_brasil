"""
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque 
e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

- **Exemplo 1:** Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
- **Exemplo 2:** Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

# Entrada
valor_saque = int(input(
    'Informe o valor do saque (mínimo é de 10 reais e' 
    +'o máximo de 600 reais): '
))

# Processamento
if valor_saque < 10 or valor_saque > 600:
    print('O valor do saque é inválido...')
    exit(1)

notas_5 = valor_saque % 10 // 5
notas_1 = valor_saque % 10 - notas_5 * 5
notas_50 = valor_saque % 100 // 10 // 5
notas_10 = (valor_saque % 100 - (notas_50 * 50)) // 10 
notas_100 = valor_saque % 1000 // 100

# Saída
print(f'Notas de 100: {notas_100}')
print(f'Notas de 50: {notas_50}')
print(f'Notas de 10: {notas_10}')
print(f'Notas de 5: {notas_5}')
print(f'Notas de 1: {notas_1}')
