"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

inicio = int(input('Digite o primeiro número: '))
fim = int(input('Digite o segundo número: '))
soma = 0

for i in range(inicio, fim + 1):
    print(i)
    soma += i

print(f'Soma: {soma}')
