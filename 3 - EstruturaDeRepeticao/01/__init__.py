"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
"""

while True:
    # Entrada
    nota = input('Digite uma nota entre 0 e 10: ')

    # Processamento
    if not nota.replace('.', '', 1).isdecimal():
        print('valor inválido.')
        continue
    
    nota = float(nota)

    if 0 <= nota and nota <= 10:
        break

    print('valor inválido.')


# Saída
print(f'Nota válida: {nota}')
