"""
Faça um Programa que peça um número correspondente a um determinado
ano e em seguida informe se este ano é ou não bissexto.
"""

# Entrada
ano = int(input('Digite o ano para saber se ele é ou não bissexto: '))

# Processamento
if not ano % 4 and ano % 100 or not ano % 400:
    bissexto = True
else:
    bissexto = False

# Saída
if bissexto:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} NÃO é bissexto!')
