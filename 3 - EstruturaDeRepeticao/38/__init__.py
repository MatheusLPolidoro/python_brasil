"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

    A.  Esse funcionário foi contratado em 1995, 
        com salário inicial de R$ 1.000,00;

    B.  Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

    C.  A partir de 1997 (inclusive), os aumentos salariais sempre 
        correspondem ao dobro do percentual do ano anterior.
        
Faça um programa que determine
o salário atual desse funcionário. Após concluir isto, altere o programa
permitindo que o usuário digite o salário inicial do funcionário.
"""

from datetime import datetime

# Entrada
salario_inicial = float(input('Salário atual: '))
ano_contratacao = 1995
percentual_aumento = .015
progressao_anual = 2

# Processamento
salario_atual = salario_inicial

for ano in range(ano_contratacao + 1, datetime.now().year):
    salario_atual += salario_atual * percentual_aumento
    if ano >= 1997:
        percentual_aumento *= progressao_anual

# Saída
print(f'Ano de contratação: {ano_contratacao}')
print(f'Salário de contratação: {salario_inicial:.2f}')
print(f'Salário atual: {salario_atual:.2f}')
