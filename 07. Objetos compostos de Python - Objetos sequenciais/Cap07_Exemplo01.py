# Os objetos compostos da linguagem Python constituem recursos muito valiosos aos programadores.
# Permitem capacidade de processamento de grandes volumes de dados, com eficiência, confiabilidade e flexibilidade.
# Estes objetos compostos também são chamados de objetos estruturados pois seu conteúdo é
# formado por elementos que podem ser acessados individualmente e também em grupo.
# No universo de objetos estruturados de Python há três que são conhecidos como Objetos Sequenciais:
# • os strings - classe str (já temos trabalhado com eles);
# • as listas - classe list;
# • as tuplas - classe tuple;

# A principal característica dos tipos sequenciais é que seus elementos são mantidos em uma
# organização baseada em um índice numérico crescente da esquerda para a direita, que começa em zero e
# sofre o incremento de um a um. Com isso, é possível ao programador acessar individualmente seus
# elementos através do uso de índices especificados entre colchetes: [ ].
# Vamos abordar primeiro a classe list, que é um dos elementos mais importantes de Python.


# LISTAS – CLASSE list
# A classe list é uma sequência. Listas são usadas para armazenar objetos de qualquer classe.
# Poderiamos representar a list como um grupo de objetos reunidos em um mesmo identificador (nome)
# e que podem ser acessados individualmente através de um índice numérico.
# Esse índice é representado pelos números de 0 a 9.

L = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
print('Exibição da lista completa')
print(L)
print('\nExibição dos elementos individuais')
i = 0
while i < len(L):
    print(L[i], end=' ')
    i = i + 1
print('\nFim do Programa')

# Exibição da lista completa
# [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
#
# Exibição dos elementos individuais
# 36 25 21 48 17 9 16 23 29 31
# Fim do Programa


# Em Python podemos fazer o programa de modo onde a lista L é pré-carregada com os valores e exibida de duas formas:
# • primeira forma: exibição da lista como completa com a função print(L);
# • segunda forma: através do laço de repetição para exibir um elemento por vez usando o índice do elemento print(L[i]);
