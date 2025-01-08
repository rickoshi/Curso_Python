# A CLASSE SET
# Conjuntos em Python são implementados através da classe set, que permite a criação de coleções
# de objetos, com as seguintes características:
#
# Elementos não repetidos
# Todos os elementos dentro de um conjunto é único, ou seja, repetição de objetos com mesmo
# conteúdo não são aceitos.
#
# Elementos não ordenados
# A ordem dos elementos não tem relevância e não é possível ordená-los. Essa ordem é definida pelo
# interpretador Python e não seguirá qualquer critério que nós, programadores, possamos pretender
#
# O conjunto é mutável
# Os conjuntos são mutáveis, ou seja, podem receber novos elementos e podem sofrer exclusão de
# elementos.
#
# Elementos são imutáveis
# Todos os elementos de um conjunto são imutáveis e, uma vez que sejam incluídos, não podem ter seu
# valor alterado. Por consequência disto, elementos mutáveis como listas, dicionários e outros conjuntos não
# podem se


# CRIAÇÃO DE UM CONJUNTO
# Os conjuntos em Python podem ser criados com o uso do comando de atribuição de duas formas como
# mostrados nas linhas a seguir:

# c1 = {16, 8, 29}
# c2 = set()

# Para criar um conjunto não vazio pode-se simplesmente usar um par de chaves {} contendo os
# elementos separados por vírgulas. Porém, para criar um conjunto vazio deve-se usar o construtor set().


# Criação de um conjunto não-vazio usando o par de chaves {}
c1 = {16, 8, 29}
print(type(c1))     # <class 'set'>
print(len(c1))      # 3
print(c1)           # {16, 8, 29}

# Criação de um conjunto vazio usando o construtor da classe set()
c2 = set()
print(type(c2))     # <class 'set'>

# Tentativa de criação de um conjunto vazio usando o par de chaves {}
c3 = {}
print(type(c3))     # <class 'dict'>
# o uso das chaves dessa forma cria um dicionário

# Criação de um conjunto não-vazio usando o construtor da classe set()
c4 = set((23, 9, 41))
print(type(c4))     # <class 'set'>
print(c4)           # {9, 41, 23}


# Nesse exemplo, no caso do objeto c3, constatamos que ao tentar usar o par de chaves na tentativa de
# criar um conjunto vazio, acabamos criando um dicionário.
# Para criar conjuntos vazio use sempre o construtor set().

# No caso do conjunto c4 vemos que se pode criar um conjunto não vazio usando o construtor da classe.
# Neste caso o construtor deve receber como parâmetro iterável, podendo ser string, tupla, lista, conjunto ou
# dicionário.
