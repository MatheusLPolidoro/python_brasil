"""
Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
"""

# Entrada
list_nums = list()
len_nums = int(input('Quantos números você quer comparar: '))

for index in range(1, len_nums + 1):
    list_nums.append(float(input(f'Digite o {index}º número: ')))

# Processamento
menor_valor = min(list_nums)
maior_valor = max(list_nums)
soma_valores = sum(list_nums)

# Saída
print(f'O menor valor é: {menor_valor}')
print(f'O maior valor é: {maior_valor}')
print(f'A soma dos valores é: {soma_valores}')
