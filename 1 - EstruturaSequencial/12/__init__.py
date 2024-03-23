"""
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
"""

# Entrada
altura = float(input('Digite a altura de uma pessoa: '))

# Processamento
peso_ideal = (72.7 * altura) - 58

# Saída
print(
    f'Para altura {altura} o peso ideal,' 
    +f' usando a formula (72.7*altura) - 58 é: {peso_ideal}'
)
