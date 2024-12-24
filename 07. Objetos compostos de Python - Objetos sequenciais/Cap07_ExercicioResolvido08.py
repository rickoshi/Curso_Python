# Enunciado: Escreva um programa que leia um string contendo três números inteiros separados por espaços em
# branco. Separe-os em objetos int, calcule sua soma e exiba na tela.

# Entrada: 26 128 44 (string com três inteiros separados por espaço em branco)

# Saída: n1 = 26
# n2 = 128
# n3 = 44
# Soma = 198

valores = input('Digite 3 inteiros separados por espaço: ')
valores = valores.split()           # usa o método .split() para serparar os valores
for i in range(len(valores)):       # itera sobre a lista valores
    valores[i] = int(valores[i])    # converte cada objeto para int
print(f'n1 = {valores[0]}')
print(f'n2 = {valores[1]}')
print(f'n3 = {valores[2]}')
print(f'Soma = {sum(valores)}')     # calcula e exibe a soma

# Digite 3 inteiros separados por espaço: 26 128 44
# n1 = 26
# n2 = 128
# n3 = 44
# Soma = 198


# Neste exemplo usamos o método .split() para separar o string, usando o caractere espaço em
# branco como critério de separação. Como resultado obtemos uma lista onde cada elemento é também um
# string. Em seguida cada um é convertido para número inteiro e exibido na tela. No final a soma dos elementos
# da lista é calculada e também exibida.


# CARACTERÍSTICAS COMUNS ÀS CLASSES DE SEQUÊNCIAS – LISTAS, TUPLAS E STRINGS
# • Ordenados: contêm elementos organizados sequencialmente de acordo com sua ordem de inserção específica.
# • Indexáveis através de um índice baseado em zero: Permitem acessar seus elementos por índices
# inteiros que começam em zero.
# • Anhinháveis: Lista e tuplas podem conter outras sequências. Desse modo que é possível criar lista
# de listas, lista de tuplas, tupla de tuplas e tupla de listas.
# • Iterável: Eles suportam iteração, então você pode percorrê-los usando um loop ou compreensão
# enquanto executa operações com cada um de seus elementos.
# • Fatiáveis: Eles suportam operações de fatiamento, o que significa que você pode extrair uma série
# de elementos de uma sequência qualquer.
# • Combináveis: Eles suportam operações de concatenação, portanto você pode combinar duas ou
# mais tuplas usando os operadores de concatenação, o que cria uma nova sequência.
