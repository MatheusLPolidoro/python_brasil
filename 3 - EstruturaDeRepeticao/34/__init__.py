"""
Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia. Um número primo é aquele que é divisível
apenas por um e por ele mesmo. Faça um programa que peça um número
inteiro e determine se ele é ou não um número primo.
"""

# Entrada
num = int(input('Digite um número inteiro para saber se é primo: '))

# Processamento
primo = True

# verificar apenas números ímpares até a raiz quadrada de num
for i in range(1, int(num ** 0.5) + 1, 2):
    if num == 2:
        break
    if num < 2 or num % 2 == 0 or (num % i == 0 and i > 1):
        primo = False
        break

# Saída
print(f"O número {num}{' ' if primo else ' não '}é primo.")
