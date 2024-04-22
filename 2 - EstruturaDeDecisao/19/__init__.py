"""
Faça um Programa que leia um número inteiro menor que 1000 
e imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades 
- Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

# Entrada
num = int(input('Informe um número inteiro menor que 1000: '))

# Processamento
unidade = num % 10
dezena = int(num % 100 / 10)
centena = int(num % 1000 / 100)

msg = ''

if centena > 1:
    msg += f'{centena} centenas, '
elif centena:
    msg += f'{centena} centena, '

if dezena > 1:
    msg += f'{dezena} dezenas e '
elif dezena:
    msg += f'{dezena} dezena e '
elif centena:
    msg += '0 dezenas e '

if unidade > 1:
    msg += f'{unidade} unidades'
elif unidade:
    msg += f'{unidade} unidade'
elif centena:
    msg += '0 unidades'

# Saída
print(f'{num} = {msg}')
