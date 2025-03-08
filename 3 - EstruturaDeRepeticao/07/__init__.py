"""
Faça um programa que leia 5 números e informe o maior número.
"""

maior_num = 0

for i in range(5):
    num = float(input('Digite um número: '))
    if num > maior_num:
        maior_num = num

print(f'O maior número é: {maior_num: .2f}')
