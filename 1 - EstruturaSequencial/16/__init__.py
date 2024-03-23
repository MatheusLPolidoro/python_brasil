"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
cada 3 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00. Informe ao usuário a
quantidades de latas de tinta a serem compradas e o preço total.
"""
from math import ceil

# Constantes
LITROS_POR_LATA = 18
CUSTO_POR_LATA = 80
LITROS_POR_METRO = 3

# Entrada
area = float(input('Digite o tamnho em m² da área a ser pintada: '))

# Processamento
litros = area / LITROS_POR_METRO
latas = ceil(litros / LITROS_POR_LATA)
preco_total = latas * CUSTO_POR_LATA

# Saída
print(
    f'Para pintar {area} m², será necessaria {latas} latas, '
    + f'sendo R$ {CUSTO_POR_LATA:.2f} por lata, o total será R$ {preco_total:.2f}'
)
