"""
Faça um Programa que pergunte quanto você ganha 
por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

ganho_hora = float(input('Quando você recebe por hora? '))
horas_mes = float(input('Quantas horas você trabalha em um mês? '))
total_salario = ganho_hora * horas_mes

print(f'O total de seu salario com {horas_mes} horas trabalhadas foi de {total_salario}')
