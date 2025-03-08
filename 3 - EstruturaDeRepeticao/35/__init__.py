"""
Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos
existentes entre 1 e um número inteiro informado pelo usuário.
"""

# Entrada
num = int(input('Digite um número inteiro: '))

# Processamento
list_primos = list()

for n in range(1, num + 1):
    if n < 2:  # 0 e 1 não são primos
        continue

    if n == 2:  # 2 é o único número primo par
        list_primos.append(str(n))
        continue

    if n % 2 == 0:  # todos os outros números pares não são primos
        continue

    primo = True
    
    # verificar apenas números ímpares até a raiz quadrada de n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            primo = False
            break

    if primo:
        list_primos.append(str(n))

# Saída
print(f"Os números primos de 1 até {num} são:\n{', '.join(list_primos)}")
