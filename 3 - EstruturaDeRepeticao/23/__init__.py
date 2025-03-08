"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número
de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de
testes (divisões) executados.
"""

# Entrada
num = int(input('Digite um número inteiro: '))

# Processamento
list_primos = list()
num_divisao = 0

for n in range(1, num + 1):
    if n < 2:  # 0 e 1 não são primos
        continue

    if n == 2:  # 2 é o único número primo par
        list_primos.append(str(n))
        continue

    num_divisao += 1

    if n % 2 == 0:  # todos os outros números pares não são primos
        continue

    primo = True
    
    for i in range(3, int(n ** 0.5) + 1, 2): # verificar apenas números ímpares até a raiz quadrada de n
        num_divisao += 1
        if n % i == 0:
            primo = False
            break

    if primo:
        list_primos.append(str(n))

# Saída
print(f"Os números primos de 1 até {num} são:\n{', '.join(list_primos)}")
print(f'Foram executadas {num_divisao} divisões')
