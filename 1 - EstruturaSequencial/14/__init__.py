"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso
(peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
de quilos além do limite e na variável multa o valor da multa que João deverá
pagar. Imprima os dados do programa com as mensagens adequadas.
"""

# Constantes
PESO_LIMITE = 50

# Entrada
peso = float(input('Digite é o peso de um peixe (Kg): '))

# Processamento
if peso > PESO_LIMITE:
    excesso = peso - PESO_LIMITE
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

# Saída
print(f'Excesso: {excesso:.3f} Kg')
print(f'Multa: {multa:.2f}')
