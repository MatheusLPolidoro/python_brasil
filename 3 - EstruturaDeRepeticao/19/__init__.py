"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

## Programa anterior

Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.

"""

# Entrada
list_nums = list()
len_nums = int(input('Quantos números você quer comparar: '))

index = 1
while index <= len_nums:
    num = float(input(f'Digite o {index}º número: '))
    if 0 <= num <= 1_000:
        list_nums.append(num)
        index += 1
    else:
        print('O número deve ser entre 0 e 1000.')

# Processamento
menor_valor = min(list_nums)
maior_valor = max(list_nums)
soma_valores = sum(list_nums)

# Saída
print(f'O menor valor é: {menor_valor}')
print(f'O maior valor é: {maior_valor}')
print(f'A soma dos valores é: {soma_valores}')
