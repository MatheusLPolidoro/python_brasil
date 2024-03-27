"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input('Digite uma letra: ').strip().upper()

if letra in ('A', 'E', 'I', 'O', 'U'):
    print(f'Letra {letra} é uma VOGAL.')
else:
    print(f'Letra {letra} é uma Consoante.')
