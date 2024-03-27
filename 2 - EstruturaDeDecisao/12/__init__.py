"""
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do
salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que
o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário
Bruto menos os descontos. O programa deverá pedir ao usuário o valor
da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

Salário Bruto até 900 (inclusive) - isento 
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Descritivo	Valor
Salário Bruto: (5 * 220)	R$ 1100,00
(-) IR (5%)	R$ 55,00
(-) INSS ( 10%)	R$ 110,00
FGTS (11%)	R$ 121,00
Total de descontos	R$ 165,00
Salário Liquido	R$ 935,00
"""

# Entrada
valor_hora = float(input('Digite o valor da sua hora trabalhada: '))
horas_mes = float(input('Digite a quantidade de horas trabalhadas no mês: '))

# Processamento
salario_bruto = valor_hora * horas_mes

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 5
elif salario_bruto <= 2500:
    ir = 5
else:
    ir = 20

valor_ir = salario_bruto * ir / 100
valor_inss = salario_bruto * 10 / 100
valor_fgts = salario_bruto * 11 / 100
total_descontos = valor_ir + valor_inss
salario_liquido = salario_bruto - total_descontos

# Saída
print(f"{'Descritivo':<35}{'Valor':<15}")
print('-' * 50)
print(
    f"{f'Salário Bruto: ({valor_hora} * {horas_mes})':<35}"
    + f'R$ {salario_bruto:<15.2f}'
)
print(f"{f'(-) IR ({ir}%):':<35}R$ {valor_ir:<15.2f}")
print(f"{f'(-) INSS (10%)':<35}R$ {valor_inss:<15.2f}")
print(f"{f'FGTS (11%)':<35}R$ {valor_fgts:<15.2f}")
print(f"{f'Total de descontos':<35}R$ {total_descontos:<15.2f}")
print(f"{f'Salário Liquido':<35}R$ {salario_liquido:<15.2f}")
