"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

# Entrada
num_notas = int(input('Digite o número de notas que deseja avaliar: '))
notas = list()

for index in range(1, num_notas + 1):
    notas.append(float(input(f'Digite a {index}º nota: ')))

# Processamento
media = sum(notas) / len(notas)

# Saída
print(f'A média aritmética é: {media:.2f}')
