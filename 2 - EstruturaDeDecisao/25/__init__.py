"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

# Entrada
tel = input('Telefonou para a vítima? [S/N]: ').upper()
local = input('Esteve no local do crime? [S/N]: ').upper()
mora_perto = input('Mora perto da vítima? [S/N]: ').upper()
devia = input('Devia para a vítima? [S/N]: ').upper()
trabalhou = input('Já trabalhou com a vítima? [S/N]: ').upper()

# Processamento
respostas_s = 0
if tel == 'S':
    respostas_s += 1
if local == 'S':
    respostas_s += 1
if mora_perto == 'S':
    respostas_s += 1
if devia == 'S':
    respostas_s += 1
if trabalhou == 'S':
    respostas_s += 1

if respostas_s == 5:
    classificacao = 'Assasino'
elif respostas_s >= 3:
    classificacao = 'Cúmplice'
elif respostas_s >= 2:
    classificacao = 'Suspeita'
else:
    classificacao = 'Inocente'

# Saída
print(classificacao)
