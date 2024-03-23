"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

# Entrada
tamanho_arquivo = float(
    input('Digite o tamanho do arquivo para download (em MB): ')
)
velocidade = float(input('Digite a velocidade de download (em Mbps): '))

# Processamento
segundos = tamanho_arquivo / velocidade / 8 # 1 byte = 8 bits
minutos = int(segundos / 60)

# Saída
print(
    f'um arquivo de {tamanho_arquivo} '
    + f'MB leva uma média de {minutos} minutos'
)
