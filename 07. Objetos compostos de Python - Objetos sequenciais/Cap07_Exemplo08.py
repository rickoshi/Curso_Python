# FATIAMENTO DE LISTAS
# O fatiamento (em inglês: slicing) é uma operação usada com frequência em Python aplicável a listas, tuplas e strings.
# Essa operação permite extrair parte da sequência de origem para produzir outra sequência.
# A construção de um fatiamento é feita como indicado na linha abaixo:

# Destino = Origem[ini:fim]

# Com um código assim a lista Destino será criada com os elementos da lista Origem, começando na
# posição ini e terminando na posição fim-1. O elemento da posição fim nunca é incluído.
# No exemplo a seguir a lista Origem tem 10 elementos e é feito o fatiamento [3:6] de modo que os
# elementos das posições 3, 4 e 5 serão incluídos na lista Destino1.
# O elemento da posição 6 ficará de fora – esteja sempre atento a isso.

Origem = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]

# primeiro caso
Destino1 = Origem[3:6]
print(Origem)               # [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
print(Destino1)             # [48, 17, 9]


# Adicionalmente o fatiamento pode conter um terceiro parâmetro, da seguinte forma:
# Destino = Origem[ini:fim:passo]

# Neste caso o terceiro parâmetro é o passo, que será usado como um "pulo" entre elementos
# sucessivos. No segundo caso do exemplo foi usado o fatiamento [1:7:2] que resulta em seleção dos
# elementos das posições 1, 3 e 5, ou seja [25, 48, 9]. Por padrão o passo é 1 quando não especificado.

# segundo caso – incluindo o passo
Destino2 = Origem[1:7:2]
print(Destino2)             # [25, 48, 9]


# Também é possível omitir os parâmetros ini e fim.
# Destino = Origem[:fim]
# No caso da omissão de ini o fatiamento é feito a partir do início da lista e é terminado em fim-1.

# terceiro caso – omitindo ini
Destino3 = Origem[:4]
print(Destino3)             # [36, 25, 21, 48]


# Destino = Origem[ini:]
# No caso da omissão de fim o fatiamento começará em ini e se estenderá até o final da lista

# quarto caso – omitindo fim
Destino4 = Origem[6:]
print(Destino4)             # [16, 23, 29, 31]


# Forma                 Interpretação
# Lst[ini:fim]          O fatiamento começa em ini e termina em fim - 1
# Lst[:fim]             O fatiamento começa no elemento 0 e termina em fim – 1
# Lst[ini:]             O fatiamento começa em ini e vai até o final da lista
# Lst[:]                O fatiamento engloba a lista inteira
# Lst[ini:fim:p]        O fatiamento começa em ini e termina em fim – 1 e tem passo p
# Lst[:fim:p]           O fatiamento começa no elemento 0 e termina em fim – 1 e tem passo p
# Lst[ini::p]           O fatiamento começa em ini e vai até o final da lista e tem passo p

# A forma de fatiamento sem parâmetros Destino = Origem[:] é de grande interesse e é detalhada na próxima seção.
