"""
Faça um Programa que peça um valor e mostre na 
tela se o valor é positivo ou negativo.
"""
valor = float(input('Digite um valor númerico: '))

if valor > 0:
    print(f'{valor} Positivo')
elif valor < 0:
    print(f'{valor} Negativo')
else:
    print('Zero')
