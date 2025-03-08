"""
Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando
a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo,
junto com suas alturas.
"""

from collections import namedtuple

# Entrada
Aluno = namedtuple('Aluno', 'numero, altura')
alunos = list()

while len(alunos) < 10:
    num = int(input('Número do aluno: '))

    if num in [aluno.numero for aluno in alunos]:
        print('Número de aluno já cadastrado')
        continue
    
    altura = float(input('Altura em centímetros: '))
    alunos.append(Aluno(num, altura))

# Processamento
mais_alto = max(alunos, key=lambda aluno: aluno.altura)
mais_baixo = min(alunos, key=lambda aluno: aluno.altura)

# Saída
print(f'Aluno mais alto: {mais_alto}')
print(f'Aluno mais baixo: {mais_baixo}')
