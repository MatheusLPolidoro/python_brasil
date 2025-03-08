"""
Foi feita uma estatística em cinco cidades brasileiras para coletar
dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

- Código da cidade;
- Número de veículos de passeio (em 1999);
- Número de acidentes de trânsito com vítimas (em 1999). 

Deseja-se saber:

- Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
- Qual a média de veículos nas cinco cidades juntas;
- Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
from statistics import mean
from collections import namedtuple

# Entrada
Cidade = namedtuple('cidade', 'codigo,veiculos,acidentes')
cidades = list()

while len(cidades) < 5:
    codigo = input('Código da cidade: ')

    if codigo in [cidade.codigo for cidade in cidades]:
        print('Já consta este código de cidade.')
        continue

    veiculos = int(input('Número de veículos de passeio (em 1999): '))
    acidentes = int(
        input('Número de acidentes de trânsito com vítimas (em 1999): ')
    )

    cidades.append(Cidade(codigo, veiculos, acidentes))

# Processamento
mais_acidente = max(cidades, key=lambda cidade: cidade.acidentes)
menos_acidente = min(cidades, key=lambda cidade: cidade.acidentes)
media_veiculos = int(mean([cidade.veiculos for cidade in cidades]))
cidades_filtro = list(filter(lambda cidade: cidade.veiculos < 2_000, cidades))
media_acidentes = int(mean([cidade.acidentes for cidade in cidades_filtro]))

# Saída
print(f'Mais acidente: {mais_acidente}')
print(f'Menos acidente: {menos_acidente}')
print(f'Média veiculos: {media_veiculos}')
print(
    f'Média acidentes nas cidades com menos '
    + f'de 2.000 veiculos de passeio: {media_acidentes}'
)
