"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

Dica: utilize uma função de arredondamento.
"""

# Entrada
num = float(input('Digite um número: '))

# Processamento / Saída
if num == round(num):
    print('Número inteiro')
else:
    print('Número decimal')
