"""
Faça um programa que calcule o valor total investido
por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs
e o valor para em cada um.
"""

# Entrada
quantidade_cds = int(input('Digite a quantidade de CDs: '))

# Processamento
cds = dict.fromkeys(list(range(1, quantidade_cds + 1)))
for cd in cds.keys():
    while True:
        valor = float(input(f'Digite o valor do {cd}º CD: '))
        if 0 < valor:
            cds[cd] = valor
            break
        print('Atenção! O valor precisa ser maior do que zero.') 

resultado = [
    f'CD: {cd} valor: {valor}' 
    for cd, valor in cds.items()
]

# Saída
print('\n'.join(resultado))
