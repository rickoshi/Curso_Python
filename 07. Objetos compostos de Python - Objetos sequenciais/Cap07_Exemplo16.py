# TUPLAS – CLASSE tuple
# Tuplas (classe tuple) são sequências imutáveis, usadas com frequência para armazenar sequencias de dados heterogêneos,
# embora nada exista nenhum impedimento para que uma tupla seja homogênea.
# A tupla é uma das classes compostas mais elementar disponível em Python.
# Simplificando um pouco pode-se pensar na tupla como sendo uma lista "só para leitura".
# Elas são usadas em situações em que queremos armazenar um número fixo de itens que não serão alterados.

# Alguns exemplos de situações em que tuplas são usadas:
# • representar coordenadas cartesianas (x, y): muito usados em jogos e gráficos;
# • cores no formato RGB (vermelho, verde, azul): muito usados em jogos e aplicações web;
# • registros em uma tabela de banco de dados (matrícula, nome, idade, endereço, etc): muito usado
# em sistemas comerciais; e assim por diante.

# A principal característica que nos leva a considerar o uso de tuplas nos nossos programas são o fato de
# que elas consomem quantidades relativamente pequenas de memória em comparação com as listas.

# O exemplo a seguir mostra como uma tupla é criada. Podemos usar dois formatos, com os dados entre parênteses,
# com no caso das tuplas T e V; ou sem os parênteses como no caso da tupla U.
# Este exemplo também mostra que tuplas podem ser heterogêneas (T e U) ou homogêneas (V).

# Também é mostrado que se pode acessar cada elemento individualmente usando o índice, bem como
# usar a tupla em uma iteração com o comando for.
# E a tentativa de alterar um elemento de T ao fazer T[0] = 26 resulta em um erro.

T = (12, 'Python', 27.3, 14)
print(type(T))      # <class 'tuple'>

U = 12, 'Python', 27.3, 14
print(type(U))      # <class 'tuple'>

V = (10, 12, 14, 16)
print(type(V))      # <class 'tuple'>

print(T[0])         # 12
print(T[1])         # Python

for dado in T:
    print(dado)
# 12
# Python
# 27.3
# 14

# T[0] = 26
# Traceback (most recent call last):
#   File "Cap07_Exemplo16.py", line 41, in <module>
#     T[0] = 26
#     ~^^^
# TypeError: 'tuple' object does not support item assignment


# O quadro a seguir mostra como essa classe é leve, quando comparada à classe list.
# Ela contém apenas dois métodos e ambos são relacionados ao acesso aos seus elementos e
# por consequência quando usada consome menos bytes da memória do computador.

# Método                            Descrição
# .count(object)                    Retorna o número de ocorrências de um objeto dentro da tupla
#                                   ex. Qtde = T.count(5)
# .index(value, [start, stop])      Retorna o índice da primeira ocorrência do objeto value dentro da tupla.
#                                   Se start e stop (opcionais) forem fornecidos o método considera
#                                   apenas seu intervalo. Caso value não esteja na tupla é gerado um erro
#                                   ex. posição = T.index(5)
