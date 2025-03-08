"""
Faça um programa que calcule o número médio de alunos por turma.Para isto,
peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

# Entrada
quantidade_turmas = int(input('Digite a quantidade de turmas: '))

# Processamento
turmas = dict.fromkeys(list(range(1, quantidade_turmas + 1)))
for turma in turmas.keys():
    while True:
        alunos = int(input(f'Digite a quantidade de alunas da {turma}º turma: '))
        if 0 < alunos <= 40:
            turmas[turma] = alunos
            break
        print('Atenção! As turmas não podem ter mais de 40 alunos.') 

resultado = [
    f'turma: {turma} alunos: {alunos}' 
    for turma, alunos in turmas.items()
]

# Saída
print('\n'.join(resultado))
