"""
Altere o programa anterior permitindo ao usuário informar
as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

while True:
    # Entrada
    habitantes_A = int(input('Número de habitantes iniciais do pais A: '))
    habitantes_B = int(input('Número de habitantes iniciais do pais B: '))

    taxa_anual_crescimento_A = float(
        input('taxa de crecimento anual do pais A: ')
    ) / 100
    taxa_anual_crescimento_B = float(
        input('taxa de crecimento anual do pais B: ')
    ) / 100

    anos = 0

    # Processamento
    while habitantes_A < habitantes_B:
        habitantes_A += habitantes_A * taxa_anual_crescimento_A
        habitantes_B += habitantes_B * taxa_anual_crescimento_B
        anos += 1

    # Saída
    print(f'Serão necessários {anos} anos.')

    if input('Repetir operação [S/N]').upper() == 'N':
        break
