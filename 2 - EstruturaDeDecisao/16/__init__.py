"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c
e fazer as consistências, informando ao usuário nas seguintes situações:

- Se o usuário informar o valor de A igual a zero, a equação não é do 
segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
- Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
- Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

# Entrada
a = float(input('Digite um número para variavel "A": '))
b = float(input('Digite um número para variavel "B": '))
c = float(input('Digite um número para variavel "C": '))

# Processamento / Saída
if not a:
    print('A equação não é do segundo grau...')
    exit(1)

delta = b ** 2 - 4 * a * c

print(f'O valor de delta é: {delta:.1f}')

if delta < 0:
    print('A equação não possui raizes reais.')
    exit(1)

raiz_real_positiva = (-(b) + delta ** .5) / (2 * a)

if not delta:
    print(f'A equação possui apenas uma raiz real: {raiz_real_positiva:.1f}')

raiz_real_negativa = (-(b) - delta ** .5) / (2 * a)

print(
    'A equação possui duas raiz reais: '
    + f'{raiz_real_positiva:.1f} e {raiz_real_negativa:.1f}'
)
