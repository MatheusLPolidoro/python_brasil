"""
Faça um programa que peça para n pessoas a sua idade,
ao final o programa devera verificar se a média de
idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

# Entrada
num_notas = int(input('Digite o número de pessoas que deseja avaliar: '))
idades = list()

for index in range(1, num_notas + 1):
    idades.append(float(input(f'Digite a idade da {index}º pessoa: ')))

# Processamento
media = sum(idades) / len(idades)

if 0 > media <= 25:
    faixa_etaria = 'jovem'
elif media <= 60:
    faixa_etaria = 'adulta'
elif media > 60:
    faixa_etaria = 'idosa'
else:
    faixa_etaria = 'inválida'

# Saída
print(f'Essa turma é {faixa_etaria}!')
