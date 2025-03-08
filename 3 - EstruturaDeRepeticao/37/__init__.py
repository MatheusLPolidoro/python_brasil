"""
Uma academia deseja fazer um senso entre seus
clientes para descobrir o mais alto, o mais baixo,
o mais gordo e o mais magro, para isto você deve fazer
um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando
o usuário digitar 0 (zero) no campo código. Ao encerrar o programa
também deve ser informados os códigos e valores do clente mais alto,
do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes
"""
from collections import namedtuple
from statistics import mean

# Entrada
Cliente = namedtuple('Cliente', 'codigo,altura,peso')
clientes = list()

while True:
    codigo = input('Código (0 para sair): ').strip()

    if codigo == '0':
        break
    
    if codigo in [cliente.codigo for cliente in clientes]:
        print('Este codigo já foi cadastrado.')
        continue

    altura = float(input('Altura: '))
    peso = float(input('Peso: '))

    clientes.append(Cliente(codigo, altura, peso))
    
# Processamento
if not clientes:
    print('Nenhum cliente para análise.')
    exit(0)

mais_alto = max(clientes, key=lambda cliente: cliente.altura)
mais_baixo = min(clientes, key=lambda cliente: cliente.altura)
mais_gordo = max(clientes, key=lambda cliente: cliente.peso)
mais_magro = min(clientes, key=lambda cliente: cliente.peso)
media_altura, media_peso = list(map(mean, list(zip(*clientes))[1:]))

# Saída
print(f'Mais alto: {mais_alto}')
print(f'Mais baixo: {mais_baixo}')
print(f'Mais gordo: {mais_gordo}')
print(f'Mais magro: {mais_magro}')
print(f'Média altura: {media_altura:.2f}')
print(f'Média peso: {media_peso:.2f}')
