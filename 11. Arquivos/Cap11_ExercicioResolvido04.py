# Enunciado: Escreva um programa que leia um arquivo de entrada, sabendo que esse arquivo
# tem um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela. Mostrar
# também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor.
# Usar um laço while e na leitura usar o método .readline()

Lst = []
arqEntr = open('entrada_er_11.4.txt', 'r')  # abre o arquivo para leitura
linha = arqEntr.readline()                  # lê a primeira linha
# print(linha)        # 128
while linha != '':
    Lst.append(int(linha))                  # converte linha para inteiro e coloca na lista
    linha = arqEntr.readline()              # lê a próxima linha
arqEntr.close()                             # fecha o arquivos
print('Valores lidos do arquivo')
print(Lst)

Soma = sum(Lst)
print(f'Soma dos valores = {Soma}')
Qtde = len(Lst)
print(f'Quantidade = {Qtde}')
print(f'Média dos valores = {Soma/Qtde}')
Minimo = min(Lst)
print(f'Mínimo dos valores = {Minimo}')
Maximo = max(Lst)
print(f'Máximo dos valores = {Maximo}')
print('Fim do Programa')

# Valores lidos do arquivo
# [128, 446, 90, 363, 185, 59, 254, 148, 241, 74]
# Soma dos valores = 1988
# Quantidade = 10
# Média dos valores = 198.8
# Mínimo dos valores = 59
# Máximo dos valores = 446
# Fim do Programa


# Nesta solução adotamos uma lógica mais clássica e própria de outras linguagens de programação.
# Então esta solução não é muito Pythônica. O objetivo aqui é didático, para que você possa enxergar como
# Python faz as coisas.
# Na leitura usamos o método .readline(), que retornará o conteúdo da linha. Na primeira linha está
# o valor 128, mas o .readline() o retorna como um texto incluindo o caractere fim de linha, ou seja, o
# objeto linha estará carregado com '128\n'. Mas isso não é motivo de preocupação pois quando fazemos a
# conversão para inteiro o caractere '\n' é eliminado. Cada valor lido é colocado na lista Lst para que na
# segunda parte possamos usar as funções de soma, tamanho, mínimo e máximo.
# Quando acaba a leitura do arquivo o método .readline() retorna um string vazio e foi isso que
# usamos para controlar o laço de leitura.
