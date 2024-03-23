"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
- Para homens: (72.7*h) - 58
- Para mulheres: (62.1*h) - 44.7
"""

# Entrada
altura = float(input('Digite a altura de uma pessoa: '))

# Processamento
peso_ideal_h = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7

# Saída
print(
    f'Para altura {altura} o peso ideal para homens,' 
    +f' usando a formula (72.7*altura) - 58 é: {peso_ideal_h}'
)
print(
    f'Para altura {altura} o peso ideal para mulheres,' 
    +f' usando a formula (62.1*h) - 44.7 é: {peso_ideal_m}'
)
