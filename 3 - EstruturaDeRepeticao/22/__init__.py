"""
Altere o programa de cálculo dos números primos,
informando, caso o número não seja primo, por quais número ele é divisível.
"""

# Entrada
num = int(input('Digite um número inteiro para saber se é primo: '))

# Processamento
list_divisiveis = list()
num_index = num

while num_index > 1:
    if not num % num_index and num != num_index:
        list_divisiveis.append(str(num_index))
    num_index -= 1

# Saída
if list_divisiveis:
    print(f'{num} não é primo, divisível por: {", ".join(list_divisiveis)}.')
else:
    print(f'{num} é primo.')
