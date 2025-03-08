"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro
que será digitado pelo usuário, mas a tabuada não deve necessariamente
iniciar em 1 e terminar em 10, o valor inicial e final devem ser
informados também pelo usuário, conforme exemplo abaixo:

    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7

    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35

Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

"""

# Entrada
num = int(input('Montar a tabuada de: '))
num_inicial = int(input('Começar por: '))
num_final = int(input('Terminar em: '))

# Processamento / Saída
if num_inicial > num_final:
    print('Número inicial maior que o número final...')
    exit(0)

print(
    f'Vou montar a tabuada de {num} começando em ' 
    +f'{num_inicial} e terminando em {num_final}:'
)

for index in range(num_inicial, num_final + 1):
    resultado = num * index
    print(f'{num} X {index} = {resultado}')
