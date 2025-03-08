"""
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

pares = 0
impares = 0
for i in range(10):
    num = float(input('Digite um número: '))
    if num % 2:
        impares += 1
    else:
        pares += 1

print(f'Total impares: {impares}\nTotal pares: {pares}')
