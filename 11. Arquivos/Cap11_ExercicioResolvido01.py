# Enunciado: Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0. Todos
# os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha.
# Usar o método .write()

arq = open('saida_er_11.1.txt', 'w')        # abre o arquivo para gravação
A = int(input('Digite um inteiro: '))
while A != 0:
    arq.write(f'{A}\n')                     # grava uma linha do arquivo
    A = int(input('Digite um inteiro: '))
arq.close()                                 # fecha o arquivo
print('Fim do Programa')

# Digite um inteiro: 10
# Digite um inteiro: 20
# Digite um inteiro: 30
# Digite um inteiro: 40
# Digite um inteiro: 0
# Fim do Programa


# Para gravar o arquivo 'saida_er_11.1.txt' usamos o método .write().
# Observe no código que o string a ser gravado no arquivo inclui o caractere de pulo de linha '\n'.
# Sem essa inclusão todos os números gravados no arquivo ficarão na mesma linha.
