"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
"""

maior = menor = total = media = 0
loop = True

while loop:
    # Entrada
    temperatura = float(input('Temperatura: '))

    # Processamento
    total += 1
    media += temperatura

    if temperatura > maior or not maior:
        maior = temperatura
    if temperatura < menor or not menor:
        menor = temperatura

    loop = input('Nova temperatura? [S/N]: ').upper() == 'S'

media = media / total

# Saída
print(f'Maior temperatura: {maior}')
print(f'Menor temperatura: {menor}')
print(f'Média de temperaturas: {media}')
