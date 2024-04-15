"""
Faça um programa que lê as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

  |Média de Aproveitamento | Conceito |
  |:-----------------------|:---------|
  |Entre 9.0 e 10.0        |       A  |
  |Entre 7.5 e 9.0         |       B  |
  |Entre 6.0 e 7.5         |       C  |
  |Entre 4.0 e 6.0         |       D  |
  |Entre 4.0 e zero        |       E  |

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for 
A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

# Entrada
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Processamento
nota_media = (nota1 + nota2) / 2
if 0 >= nota_media < 4:
    conceito = 'E'
elif 4 >= nota_media < 6:
    conceito = 'D'
elif 6 >= nota_media < 7.5:
    conceito = 'C'
elif 7.5 >= nota_media < 9:
    conceito = 'B'
elif 9 >= nota_media <= 10:
    conceito = 'A'
else:
    conceito = 'Inválido'

if conceito in ('A', 'B', 'C'):
    resultado = 'APROVADO'
else:
    resultado = 'REPROVADO'

# Saída
print(f'Conceito: {conceito} | Resultado: {resultado}')
