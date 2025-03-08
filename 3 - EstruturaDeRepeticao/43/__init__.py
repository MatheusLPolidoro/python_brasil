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
from collections import namedtuple, defaultdict

# Preparação
locale.setlocale(locale.LC_MONETARY, 'pt_BR')

Item = namedtuple('Item', 'codigo,especificacao,preco,quantidade,total')

cardapio = [
    Item(100, 'Cachorro Quente', 1.20, 0, 0),
    Item(101, 'Bauru Simples', 1.30, 0, 0),
    Item(102, 'Bauru com ovo', 1.50, 0, 0),
    Item(103, 'Hambúrguer', 1.20, 0, 0),
    Item(104, 'Cheeseburguer', 1.30, 0, 0),
    Item(105, 'Refrigerante', 1.00, 0, 0)
]

# Exibição
print('▬' * 35)
print('Cardápio'.center(35))
print('▬' * 35)
print('Código  | Especificação   | Preço')
print('-' * 35)

for item in cardapio:
    preco_formatado = locale.currency(item.preco, 'R$', grouping=True)
    print(f"{item.codigo:<8}| {item.especificacao:<16}| {preco_formatado:<8}")

print('')

# Entrada
pedido = defaultdict(Item)

while True:
    codigo = int(input(' → Código do pedido: '))

    if codigo in pedido.keys():
        item: Item = pedido[codigo]
        mudar_qtd = input(
            f'Você já pediu {item.quantidade} {item.especificacao},' 
            + ' deseja mudar a quantidade? [S/N]: '
        ).upper()

        if mudar_qtd != 'S':
            print(' ♦ Ok, faça outro pedido.')
            continue

        quantidade = (
            int(input(f' → Nova quantidade de {item.especificacao}: '))
        )
    else:
        item: Item = next(
            filter(lambda item: item.codigo == codigo, cardapio), None
        )

        if not item:
            print(' ø Não consta este código no cardápio.\n')
            continue

        quantidade = int(input(f' → Quantidade de {item.especificacao}: '))

    # Processamento
    item = item._replace(
        quantidade=quantidade, total=item.preco * quantidade
    )

    pedido[codigo] = item

    sair = input('\nDeseja pedir mais alguma coisa? [S/N]: ').upper()

    if sair == 'N':
        break

valor_total = sum([item.total for item in pedido.values()])

# Saída
print('▬' * 70)
print('Nota do pedido'.center(70))
print('▬' * 70)
print('Código  | Especificação   | Preço unitario | Quantidade | Total')
print('-' * 70)

for item in pedido.values():
    preco = locale.currency(item.preco, 'R$', grouping=True)
    total = locale.currency(item.total, 'R$', grouping=True)
    print(
        f'{item.codigo:<8}| {item.especificacao:<16}|'
        + f' {preco:<15}| {item.quantidade:<11}| {total}'
    )

print('▬' * 70)
total = locale.currency(valor_total, 'R$', grouping=True)
print(f'VALOR TOTAL | '.rjust(58) + total)
print('▬' * 70)
