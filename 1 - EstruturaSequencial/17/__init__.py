"""
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada.Considere que a cobertura da tinta
é de 1 litro para cada 6 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00 ou em
galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário
as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:

 - comprar apenas latas de 18 litros;
 - comprar apenas galões de 3,6 litros;
 - misturar latas e galões, de forma que o desperdício de tinta
   seja menor. Acrescente 10% de folga e sempre arredonde os
   valores para cima, isto é, considere latas cheias.
"""
from math import ceil

# Constantes
LITROS_POR_LATA = 18
LITROS_POR_GALAO = 3.6
CUSTO_LATA = 80
CUSTO_GALAO = 25
LITROS_POR_METRO = 6

# Entrada
area = float(input('Digite a área em m² a ser pintada: '))

# Processamento

# Acrescente 10% de folga (110% = 1.1)
litros = area / LITROS_POR_METRO * 1.1

# comprar apenas latas de 18 litros;
latas = ceil(litros / LITROS_POR_LATA)

# comprar apenas galões de 3,6 litros;
galoes = ceil(litros / LITROS_POR_GALAO)

# misturar latas e galões, de forma que o desperdício de tinta seja menor.
latas_misto = int(litros / LITROS_POR_LATA)
galoes_misto = ceil((litros - latas_misto * LITROS_POR_LATA) / LITROS_POR_GALAO)

# calculo dos preços
valor_latas = latas * CUSTO_LATA
valor_galoes = galoes * CUSTO_GALAO

valor_latas_misto = latas_misto * CUSTO_LATA
valor_galoes_misto = galoes_misto * CUSTO_GALAO

valor_misto = valor_latas_misto + valor_galoes_misto

# Saída
print(f'Somente Latas: {latas} | valor de R$ {valor_latas:.2f}')
print(f'Somente Galões: {galoes} | valor de R$ {valor_galoes:.2f}')
print(
    f'Misturando Latas com Galões.\nLatas: {latas_misto}' 
    + f'\nGalões: {galoes_misto}\nvalor de R$ {valor_misto:.2f}'
)
