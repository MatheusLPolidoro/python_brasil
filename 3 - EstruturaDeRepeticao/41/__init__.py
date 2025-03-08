"""
Faça um programa que receba o valor de uma
dívida e mostre uma tabela com os seguintes dados: 

- valor da dívida
- valor dos juros 
- quantidade de parcelas
- valor da parcela
"""

# Entrada
divida = float(input('Digite o valor da dívida: R$ '))
juros = 0

print(
    f'Valor da Dívida | Valor dos Juros | '
    +'Quantidade de Parcelas | Valor da Parcela'
)
print('-' * 78)

# Processamento
for parcelas in [1, 3, 6, 9, 12]:
    valor_juros = divida * juros
    divida += valor_juros
    parcela = int(divida / parcelas)

    # Saída
    print(
        f'R$ {divida:<13.2f}| % {int(juros * 100):<14}'
        + f'| {parcelas:<23}| R$ {parcela:.2f}'
    )

    if parcelas == 1:
        juros = .1
    else:
        juros += .05
