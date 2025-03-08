"""
O cardápio de uma lanchonete é o seguinte:

Especificação   |Código  |Preço
----------------|--------|------
Cachorro Quente |100     |R$ 1,20
Bauru Simples   |101     |R$ 1,30
Bauru com ovo   |102     |R$ 1,50
Hambúrguer      |103     |R$ 1,20
Cheeseburguer   |104     |R$ 1,30
Refrigerante    |105     |R$ 1,00

Faça um programa que leia o código dos itens
pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade)
e o total geral do pedido. Considere que o cliente deve informar
quando o pedido deve ser encerrado.
"""
import locale
from collections import namedtuple

locale.setlocale(locale.LC_MONETARY, 'pt_BR')

Item = namedtuple('Item', 'especificacao,codigo,preco,quantidade,total')

cardapio = [
    Item('Cachorro Quente', 100, 1000.20, 0, 0),
    Item('Bauru Simples', 101, 1.30, 0, 0),
    Item('Bauru com ovo', 102, 1.50, 0, 0),
    Item('Hambúrguer', 103, 1.20, 0, 0),
    Item('Cheeseburguer', 104, 1.30, 0, 0),
    Item('Refrigerante', 105, 1.00, 0, 0)
]

print('▬' * 35)
print('Cardápio'.center(35))
print('▬' * 35)
print('Especificação   | Código | Preço')
print('-' * 35)

for item in cardapio:
    preco_formatado = locale.currency(item.preco, 'R$', grouping=True)
    print(f"{item.especificacao:<16}|{item.codigo:.<8}| {preco_formatado:<8}")

print('')

# Entrada
pedido = list()
while True:
    codigo = int(input(' → Código do pedido: '))
    item: Item = next(filter(lambda item: item.codigo == codigo, cardapio), None)

    if not item:
        print(' ø Não consta este código no cardapio.\n')
        continue

    quantidade = int(input(f' → Quantidade de {item.especificacao}: '))

    # Processamento
    item = item._replace(
        quantidade=quantidade, total=item.preco * quantidade
    )

    pedido.append(item)

    sair = input('\nDeseja pedir mais alguma coisa? [S/N]: ').upper()

    if sair == 'N':
        break

# Saída
print(pedido)
