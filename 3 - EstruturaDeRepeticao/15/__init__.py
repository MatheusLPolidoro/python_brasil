"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n-ésimo termo.
"""

n = int(input('Digite o último termo de fibonacci: '))

anterior = 1
atual = 0

while n > atual:
    atual, anterior = atual + anterior, atual
    print(atual)
