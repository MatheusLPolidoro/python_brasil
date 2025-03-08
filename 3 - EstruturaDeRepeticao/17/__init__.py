"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
"""
from functools import reduce

# Entrada
num_fat = int(input('Digite um número inteiro para saber seu fatorial: '))

# Processamento
list_nums = list(range(num_fat, 0, -1))

if list_nums:
    result = reduce(lambda x, y: x * y, list_nums)
else:
    result = 0

# Saída
print(f"{num_fat}! = {' . '.join(map(str, list_nums))} = {result}")
