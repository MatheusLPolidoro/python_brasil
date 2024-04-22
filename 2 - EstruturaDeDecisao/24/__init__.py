"""
Faça um Programa que leia 2 números e em seguida pergunte
ao usuário qual operação ele deseja realizar. O resultado
da operação deve ser acompanhado de uma frase que diga se o número é:
- par ou ímpar;
- positivo ou negativo;
- inteiro ou decimal.
"""

# Entrada
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
operacao = input('Digite qual operação quer realizar (+, -, *, /): ')

# Processamento
if operacao == '+':
    resultado = n1 + n2
elif operacao == '-':
    resultado = n1 - n2
elif operacao == '*':
    resultado = n1 * n2
elif operacao == '/':
    resultado = n1 / n2
else:
    print('Operação inválida...')
    exit(1)

if resultado % 2:
    par_impar = 'ímpar'
else:
    par_impar = 'par'

if resultado > 0:
    positivo_negativo = 'positivo'
else:
    positivo_negativo = 'negativo'

if resultado == round(resultado):
    inteiro_decimal = 'inteiro'
else:
    inteiro_decimal = 'decimal'

# Saída
print(f'{n1} {operacao} {n2} = {resultado}')
print(f'Número {par_impar}')
print(f'Número {positivo_negativo}')
print(f'Número {inteiro_decimal}')
