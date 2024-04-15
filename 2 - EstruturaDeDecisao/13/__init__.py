"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
# Entrada
num_semana = int(input('Digite um número para saber a qual data da semana ele pertence: '))

# Processamento
if num_semana == 1:
    dia_semana = 'Domingo'
elif num_semana == 2:
    dia_semana = 'Segunda'
elif num_semana == 3:
    dia_semana = 'Terça'
elif num_semana == 4:
    dia_semana = 'Quarta'
elif num_semana == 5:
    dia_semana = 'Quinta'
elif num_semana == 6:
    dia_semana = 'Sexta'
elif num_semana == 7:
    dia_semana = 'Sabado'
else:
    dia_semana = 'Inválido'

# Saída
print(f'O dia da semana é {dia_semana}.')
