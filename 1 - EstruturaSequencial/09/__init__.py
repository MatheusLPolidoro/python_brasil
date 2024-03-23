"""
Faça um Programa que peça a temperatura em graus Fahrenheit, 
transforme e mostre a temperatura em graus Celsius.
"""

fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))

celsius = (fahrenheit - 32) * 5 / 9

print(f'fahrenheit: {fahrenheit: .2f}\ncelsius: {celsius: .2f}')
