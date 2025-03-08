"""
Supondo que a população de um país A seja da ordem de 80.000
habitantes com uma taxa anual de crescimento de 3% e que a população
de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários
para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
"""

# Entrada
habitantes_A = 80_000
habitantes_B = 200_000

taxa_anual_crescimento_A = 0.03
taxa_anual_crescimento_B = 0.015

anos = 0

# Processamento
while habitantes_A < habitantes_B:
    habitantes_A += habitantes_A * taxa_anual_crescimento_A
    habitantes_B += habitantes_B * taxa_anual_crescimento_B
    anos += 1

# Saída
print(f'Serão necessários {anos} anos.')
