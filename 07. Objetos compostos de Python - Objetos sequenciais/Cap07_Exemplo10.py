# MÉTODOS DA CLASSE list
# A classe list tem um bom conjunto de métodos que nos auxiliam a manipular seus elementos.

# Método                        Descrição
# .append(object)               Acrescenta um objeto ao final da lista
#                               ex. L.append(5)
A = []
A.append(81)
print(A)        # [81]
A.append(17)
A.append(49)
A.append(53)
print(A)        # [81, 17, 49, 53]


# .clear()                      Limpa a lista, removendo todos seus elementos
#                               ex. L.clear()
A.clear()
print(A)        # []


# .copy()                       Produz uma cópia da lista L. Usar este método é uma alternativa ao uso
#                               do fatiamento mostrado na seção anterior
#                               ex. NovaLista = L.copy()
A = [81, 17, 49, 53]
print(A)        # [81, 17, 49, 53]
B = A.copy()
print(B)        # [81, 17, 49, 53]
print(id(A))    # 1941490153408
print(id(B))    # 1941489832320


# .count(object)                Retorna o número de ocorrências de um objeto dentro da lista
#                               ex. Qtde = L.count(5)
print(A.count(78))      # 0
print(A.count(81))      # 1
A.append(81)
print(A)                # [81, 17, 49, 53, 81]
n = A.count(81)
print(n)                # 2


# .extend(iterable)             Expande a lista acrescentando a ela todos os elementos contidos no
#                               objeto iterable passado como parâmetro
#                               ex. L.extend(OutraLista)
B = [1, 2, 3, 4]
print(B)        # [1, 2, 3, 4]
print(A)        # [81, 17, 49, 53, 81]
A.extend(B)
print(A)        # [81, 17, 49, 53, 81, 1, 2, 3, 4]
print(B)        # [1, 2, 3, 4]


# .index(value, [start, stop])  Retorna o índice da primeira ocorrência do objeto value dentro da lista.
#                               Se start e stop (opcionais) forem fornecidos o método considera
#                               apenas seu intervalo. Caso value não esteja na lista é gerado um erro
#                               ex. posição = L.index(5)
print(A.index(17))      # 1
print(A.index(49))      # 2
# A.index(50)           # ValueError: 50 is not in list
print(50 in A)          # False
print(81 in A)          # True
print(A.count(81))      # 2
print(A.index(81, 1))  	# 4


# .insert(index, object)        Insere o objeto fornecido na posição dada por index, deslocando todos
#                               os demais para a direita
#                               ex. L.insert(2, 30)
print(A)        # [81, 17, 49, 53, 81, 1, 2, 3, 4]
A.insert(1, 195)
print(A)        # [81, 195, 17, 49, 53, 81, 1, 2, 3, 4]
A.insert(0, 2)
print(A)        # [2, 81, 195, 17, 49, 53, 81, 1, 2, 3, 4]
print(len(A))   # 11
A.insert(15, 35)
print(A)        # [2, 81, 195, 17, 49, 53, 81, 1, 2, 3, 4, 35]


# .pop(index)                   Retorna o elemento que está na posição dada por index e o remove da
#                               lista.
#                               ex. L.pop(0)
print(A)        # [2, 81, 195, 17, 49, 53, 81, 1, 2, 3, 4, 35]
A.pop(0)
print(A)        # [81, 195, 17, 49, 53, 81, 1, 2, 3, 4, 35]
R = A.pop(4)
print(R)        # 53
print(A)        # [81, 195, 17, 49, 81, 1, 2, 3, 4, 35]
R = A.pop(-1)   # O valor padrão da função pop é -1, então .pop() e .pop(-1) são similares
print(R)        # 35
print(A)        # [81, 195, 17, 49, 81, 1, 2, 3, 4]


# .remove(value)                Remove da lista a primeira ocorrência de value . Se o valor não estiver
#                               na lista gera um erro.
#                               ex. L.remove(5)
print(A)        # [81, 195, 17, 49, 81, 1, 2, 3, 4]
A.remove(17)
print(A)        # [81, 195, 49, 81, 1, 2, 3, 4]
# A.remove(17)    # ValueError: list.remove(x): x not in list
A.remove(81)    # Remove a primeira ocorrência
print(A)        # [195, 49, 81, 1, 2, 3, 4]


# .reverse()                    Inverte a posição dos elementos dentro da lista, o primeiro valor passa a
#                               ser o último, o segundo passa a penúltimos e assim por diante. Não
#                               retorna nada pois inverte a própria lista.
#                               ex. L.reverse()
A = [2, 81, 195, 17, 49, 53, 81, 1, 2, 3, 4, 35]
print(A)        # [2, 81, 195, 17, 49, 53, 81, 1, 2, 3, 4, 35]
A.reverse()
print(A)        # [35, 4, 3, 2, 1, 81, 53, 49, 17, 195, 81, 2]
A.reverse()
print(A)        # [2, 81, 195, 17, 49, 53, 81, 1, 2, 3, 4, 35]


# .sort(...)                    Ordena a lista, colocando-a em ordem crescente ou decrescente. Não
#                               retorna nada, pois ordena a própria lista.
#                               ex. L.sort() # ordem crescente
#                               L.sort(reverse=True) # ordem decrescente
#                               Observação:
#                               1. Cuidado ao usar o método .sort() com listas heterogêneas. Se o
#                               interpretador Python não conseguir definir a forma de ordenação
#                               entre os vários elementos ele irá falhar.
A.sort()
print(A)        # [1, 2, 2, 3, 4, 17, 35, 49, 53, 81, 81, 195]
A.sort(reverse=True)
print(A)        # [195, 81, 81, 53, 49, 35, 17, 4, 3, 2, 2, 1]
