"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
qtd_nums = 5
soma = 0

for i in range(qtd_nums):
    soma += float(input('Digite um número: '))

media = soma / qtd_nums

print(f'Soma: {soma:.2f}')
print(f'Média: {media:.2f}')
