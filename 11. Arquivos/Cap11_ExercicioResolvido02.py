# Enunciado: Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos
# os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com
# 3 casas decimais. Usar o método .write()

arq = open('saida_er_11.2.txt', 'w')        # abre o arquivo para gravação
A = float(input('Digite um real: '))
while A != 0:
    arq.write(f'{A:.3f}\n')                 # grava uma linha do arquivo
    A = float(input('Digite um real: '))
arq.close()                                 # fecha o arquivo
print('Fim do Programa')

# Digite um real: 7.32
# Digite um real: 18.6
# Digite um real: 0.414
# Digite um real: 16.379
# Digite um real: 0
# Fim do Programa


# Esta solução, muito parecida com a anterior tem a única diferença
# no formato dos números que são gravados no arquivo de saída.
