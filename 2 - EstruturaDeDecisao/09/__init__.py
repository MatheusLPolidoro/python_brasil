"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))


if n1 >= n2 >= n3:
    print(f'{n1}\n{n2}\n{n3}')
elif n1 >= n3 >= n2:
    print(f'{n1}\n{n3}\n{n2}')
elif n2 >= n1 >= n3:
    print(f'{n2}\n{n1}\n{n3}')
elif n2 >= n3 >= n1:
    print(f'{n2}\n{n3}\n{n1}')
elif n3 >= n1 >= n2:
    print(f'{n3}\n{n1}\n{n2}')
elif n3 >= n2 >= n1:
    print(f'{n3}\n{n2}\n{n1}')

print(*sorted((n1, n2, n3), reverse=True)) # sem utilizar estrutura de decisão
