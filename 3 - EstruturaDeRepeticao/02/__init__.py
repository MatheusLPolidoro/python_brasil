"""
Faça um programa que leia um nome de usuário e a sua senha
e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

while True:
    # Entrada
    nome = input('Usuário: ')
    senha = input('Senha: ')

    # Processamento
    if nome != senha:
        break

    print('Erro, usuário e senha inválidos.')

# Saída
print('Usuário e senha válidos.')
