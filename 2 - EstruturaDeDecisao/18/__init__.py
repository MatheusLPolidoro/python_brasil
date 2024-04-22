"""
Faça um Programa que peça uma data no formato dd/mm/aaaa 
e determine se a mesma é uma data válida.
"""
# Entrada
data = input('Informe uma data no formato "dd/mm/aaaa": ')

# Processamento
dia, mes, ano = data.split('/')
dia, mes, ano = int(dia), int(mes), int(ano)

if mes in (1, 3, 5, 7, 8, 10, 12):
    dias = 31
elif mes in (4, 6, 9, 11):
    dias = 31
elif mes == 2:
    # definição de dias para anos bissextos
    if not ano % 4 and ano % 100 or not ano % 400:
        dias = 29
    else:
        dias = 28 
else:
    dias = -1

if 0 < dias >= dia:
    data_valida = True
else:
    data_valida = False

# Saída
if data_valida:
    print(f'A data passada é uma data valida: {data}!')
else:
    print(f'O valor passado não é uma data: {data}...')
