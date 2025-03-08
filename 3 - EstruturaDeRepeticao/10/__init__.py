"""
Faça um programa que receba dois números inteiros e gere os números
inteiros que estão no intervalo compreendido por eles.
"""

inicio = int(input('Digite o primeiro número: '))
fim = int(input('Digite o segundo número: '))

for i in range(inicio, fim + 1):
    print(i)
