"""
Altere o programa de cálculo do fatorial, 
permitindo ao usuário calcularo fatorial várias vezes
e limitando o fatorial a números inteiros positivos e menores que 16.
"""
from functools import reduce

opcao = 'S'
while opcao == 'S':
    # Entrada
    num_fat = int(input('Digite um número inteiro para saber seu fatorial: '))

    if 0 >= num_fat or num_fat >= 16:
        print('o número deve ser inteiro positivo e menor que 16.')
        continue

    # Processamento
    list_nums = list(range(num_fat, 0, -1))
    result = reduce(lambda x, y: x * y, list_nums)

    # Saída
    print(f"{num_fat}!={'.'.join(map(str, list_nums))}={result}")

    opcao = input('Deseja calcular novamente [S/N]: ').upper()
