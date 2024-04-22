"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
- A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

# Entrada
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

# Processamento
media = (nota1 + nota2 + nota3) / 3

if media == 10:
    resultado = 'Aprovado com Distinção'
elif media >= 7:
    resultado = 'Aprovado'
elif media < 7 :
    resultado = 'Reprovado'

# Saída
print(resultado)
