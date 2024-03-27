"""
As Organizações Tabajara resolveram dar um aumento de
salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador
e o reajuste segundo o seguinte critério, baseado no
salário atual:

- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:

- salário antes do reajuste;
- percentual de aumento aplicado;
- valor do aumento;
- novo salário, após o aumento.
"""

# Entrada
salario = float(input('Digite o salário do colaborador: '))

# Processamento
if 0 < salario <= 280:
    aumento = 20
elif 0 < salario <= 700:
    aumento = 15
elif 0 < salario <= 1500:
    aumento = 10
elif 0 < salario:
    aumento = 5
else:
    aumento = 0

valor_aumento = salario * aumento / 100
novo_salario = salario + valor_aumento

# Saída
print(f'Salário antes do reajuste: {salario}')
print(f'Percentual de aumento aplicado: {aumento}%')
print(f'Valor do aumento: {valor_aumento}')
print(f'Novo salário, após o aumento: {novo_salario}')
