"""
Faça um Programa que leia três números e mostre o maior deles.
"""

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
elif n3 >= n1 and n3 >= n2:
    print(n3)
