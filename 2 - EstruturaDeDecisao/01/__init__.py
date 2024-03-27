"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print(f'Maior: {n1}')
elif n1 < n2:
    print(f'Maior: {n2}')
else:
    print(f'Números iguais.')
