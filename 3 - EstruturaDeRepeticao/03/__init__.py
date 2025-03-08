"""
Faça um programa que leia e valide as seguintes informações:

1. Nome: maior que 3 caracteres;
2. Idade: entre 0 e 150;
3. Salário: maior que zero;
4. Sexo: 'f' ou 'm';
5. Estado Civil: 's', 'c', 'v', 'd';
"""

# 1. Nome: maior que 3 caracteres;
while True:
    # Entrada
    nome = input('Nome: ')
    # Processamento
    if len(nome) > 3:
        break

    print('Nome inválido.')


# 2. Idade: entre 0 e 150;
while True:
    # Entrada
    idade = input('Idade: ')
    # Processamento
    if idade.isdecimal():
        idade = int(idade)
        if 0 <= idade <= 150:
            break

    print('Idade inválida.')


# 3. Salário: maior que zero;
while True:
    # Entrada
    salario = input('Salário: ')
    # Processamento
    if salario.replace('.', '', 1).isdecimal():
        salario = float(salario)
        if salario > 0:
            break

    print('Salário inválido.')

# 4. Sexo: 'f' ou 'm';
while True:
    # Entrada
    sexo = input('Sexo [M/F]: ').upper()
    # Processamento
    if sexo in ('M', 'F'):
        break

    print('Sexo invalido.')

# 5. Estado Civil: 's', 'c', 'v', 'd';
while True:
    # Entrada
    estado_civil = input('Estado Civil [S/C/V/D]: ').upper()
    # Processamento
    if estado_civil in ('S', 'C', 'V', 'D'):
        break

    print('Estado Civil invalido.')

# Saída
print('-' * 30)
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: {salario}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {estado_civil}')
