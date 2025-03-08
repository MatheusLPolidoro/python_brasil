"""
Faça um programa que leia uma quantidade indeterminada de números positivos
e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.
"""

# Entrada
passos = 25
filtros = [(f + 1 if f else f, f + passos) for f in range(0, 100, passos)]
nums = list()

while True:
    num = int(input('Digite um número (número negativo para sair): '))
    if num < 0:
        break
    nums.append(num)

# Processamento / Saída
for start, end in filtros:
    contagem = sum(start <= num <= end for num in nums)
    print(f'Entre {start} e {end}: {contagem}')
