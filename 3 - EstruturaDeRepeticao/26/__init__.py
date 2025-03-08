"""
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número
de votos de cada candidato.
"""

# Entrada
num_eleitores = int(input('Digite o número total de eleitores: '))

# Processamento
votos = {'1': 0, '2': 0, '3': 0}

for eleitor in range(1, num_eleitores + 1):
    print(f'Olá, você é o {eleitor}º eleitor.')
    while True:
        voto = input('Digite seu voto (1, 2 ou 3): ')
        if voto in votos.keys():
            votos[voto] += 1
            break
        print('Atenção! O voto deve ser apenas para os canditados 1, 2 ou 3')

resultado = [
    f'canditado: {canditado} votos: {voto}' 
    for canditado, voto in votos.items()
]

# Saída
print('\n'.join(resultado))
