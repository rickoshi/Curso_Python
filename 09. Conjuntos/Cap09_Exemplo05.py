# MÉTODOS DA CLASSE set
# A classe set tem um conjunto de métodos que nos permitem executar operações com seus elementos.
# O quadro a seguir mostra todos eles

c = set()
print(c)            # set()
print(type(c))      # <class 'set'>
print(len(c))       # 0

# Método                            Descrição
# .add(hashable object)             Acrescenta um objeto ao conjunto. Se o objeto não é hashable
#                                   ocorre um TypeError
c.add(85)
print(c)        # {85}
c.add(190)
c.add(32)
c.add(76)
print(c)        # {32, 76, 85, 190}


# .clear()                          Remove todos os elementos do conjunto.
c.clear()
print(c)        # set()


# .copy                             Retorna uma cópia do conjunto.
c = {36, 77, 81, 43, 18}
print(c)        # {81, 18, 36, 43, 77}
print(id(c))    # 2755722796768
d = c.copy()
print(d)        # {81, 18, 36, 43, 77}
print(id(d))    # 2755722792960


# .difference(conjuntos)            Retorna um novo conjunto contendo a diferença de dois ou
#                                   mais conjuntos passados como parâmetro.
c1 = {26, 32, 45, 58, 63}
c2 = {19, 34, 58, 67, 82, 63}
print(c1.difference(c2))    # {32, 26, 45}


# .difference_update(conjuntos)     Atualiza o conjunto, removendo de seus elementos os que
#                                   estejam nos conjuntos passados como parâmetro.
print(c1)       # {32, 58, 26, 45, 63}
c1.difference_update(c2)
print(c1)       # {32, 26, 45}


# .discard(object)                  Se o parâmetro estiver presente no conjunto, então o remove,
#                                   caso não esteja não faz nada.
print(c2)       # {34, 67, 82, 19, 58, 63}
c2.discard(58)
c2.discard(99)  # 99 não existe no conjunto
print(c2)       # {34, 67, 82, 19, 63}


# .intersection(objects)            Retorna um novo conjunto contendo a interseção de dois ou
#                                   mais conjuntos.
print(c1.intersection(c2))  # set()
c1.add(82)
c1.add(34)
print(c1)       # {32, 82, 34, 26, 45}
print(c2)       # {34, 67, 82, 19, 63}
print(c1.intersection(c2))  # {34, 82}


# .intersection_update(objects)     Atualiza o conjunto com a interseção entre seus elementos e
#                                   os conjuntos passados como parâmetro.
print(c1)       # {32, 82, 34, 26, 45}
c1.intersection_update(c2)
print(c1)       # {34, 82}


# .isdisjoint(object)               Retorna True se os dois conjuntos têm interseção vazia. False
#                                   caso contrário.
c1.add(50)
c1.add(88)
c1.add(17)
print(c1)       # {34, 17, 50, 82, 88}
print(c2)       # {34, 67, 82, 19, 63}
print(c1.isdisjoint(c2))    # False
c1.discard(34)
c1.discard(82)
print(c1)                   # {17, 50, 88}
print(c2)                   # {34, 67, 82, 19, 63}
print(c1.isdisjoint(c2))    # True


# .issubset(object)                 Retorna True se o conjunto é está contido no conjunto passado
#                                   como parâmetro.
print(c1.issubset(c2))  # False
c2.add(17)
c2.add(50)
c2.add(88)
print(c1)       # {17, 50, 88}
print(c2)       # {67, 17, 82, 19, 88, 34, 50, 63}
print(c1.issubset(c2))  # True


# .issuperset(object)               Retorna True se o conjunto contém todos os elementos no
#                                   conjunto passado como parâmetro.
print(c1.issuperset(c2))    # False
print(c2.issuperset(c1))    # True


# .pop()                            Remove e retorna um elemento arbitrário do conjunto.
#                                   Se o conjunto estiver vazio, gera uma exceção KeyError.
print(c1)       # {17, 50, 88}
c1.pop()
print(c1)       # {50, 88}
a = c1.pop()
print(a)        # 50
print(c1)       # {88}


# .remove(object)                   Remove do conjunto um elemento que seja seu membro. Caso
#                                   contrário, gera uma exceção KeyError.
print(c2)           # {67, 17, 82, 19, 88, 34, 50, 63}
c2.remove(17)
print(c2)           # {67, 82, 19, 88, 34, 50, 63}
# c2.remove(99)     # KeyError: 99
print(99 in c2)     # False
print(50 in c2)     # True
c2.remove(50)
print(c2)           # {67, 82, 19, 88, 34, 63}


# .union(objects)                   Retorna um novo conjunto com a união o conjunto com o s
#                                   parâmetros passados.
c1 = {50, 16, 39, 88, 67}
print(c1)                   # {16, 50, 67, 39, 88}
print(len(c1))              # 5
print(c2)                   # {67, 82, 19, 88, 34, 63}
print(len(c2))              # 6
print(c1.union(c2))         # {34, 67, 39, 16, 50, 82, 19, 88, 63}
print(len(c1.union(c2)))    # 9


# .symmetric_difference(object)     Retorna um novo conjunto contendo a diferença simétrica de
#                                   dois conjuntos.
intersec = c1.intersection(c2)
print(intersec)     # {88, 67}
uniao = c1.union(c2)
print(uniao)        # {34, 67, 39, 16, 50, 82, 19, 88, 63}
print(c1.symmetric_difference(c2))  # {16, 82, 19, 34, 39, 50, 63}
# Os valores mostrados estão ou em um conjunto ou em outro, mas não em ambos


# .symmetric_difference_update(object)  Atualiza o conjunto com a diferença simétrica de seus
#                                       elementos com o conjunto passado como parâmetro
c3 = c1.copy()
print(c3)       # {16, 50, 67, 39, 88}
c3.symmetric_difference_update(c2)
print(c3)       # {16, 50, 82, 19, 34, 39, 63}


# .update(objects)                  Atualiza o conjunto com a união de seus elementos com os
#                                   elementos dos conjuntos passados como parâmetro.
print(c1)       # {16, 50, 67, 39, 88}
print(c2)       # {67, 82, 19, 88, 34, 63}
c1.update(c2)
print(c1)       # {34, 67, 39, 16, 50, 82, 19, 88, 63}
# Basicamente a versão _update do union()
# Em vez de retornar um objeto, atualiza o próprio conjunto
