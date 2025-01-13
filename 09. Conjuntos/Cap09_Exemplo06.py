# OPERAÇÕES COM CONJUNTOS
# Além dos métodos, também estão definidos operadores que podem ser usados com conjuntos.
# Quatro desses operadores são equivalentes a quatro métodos já descritos.

A = set('ANTONIO CARLOS')
print(A)        # {'T', 'I', 'A', ' ', 'S', 'C', 'N', 'R', 'L', 'O'}
B = set('JOSÉ CARLOS')
print(B)        # {'J', 'A', ' ', 'S', 'C', 'É', 'R', 'L', 'O'}

# Operação          Operador            Descrição
# Diferença         A – B               Retorna todos os valores de A que não
#                                       estão em B. Equivale ao método .difference()
print(A - B)    # {'I', 'T', 'N'}
print(B - A)    # {'J', 'É'}


# União             A | B               Retorna a união de A com B
#                                       Equivale ao método .union()
print(A | B)    # {'S', 'O', 'L', 'É', 'A', 'N', 'C', 'T', 'I', ' ', 'J', 'R'}


# Interseção        A & B               Retorna a interseção de A com B
#                                       Equivale ao método .intersection()
print(A & B)    # {'R', 'A', 'C', 'S', ' ', 'O', 'L'}


# Diferença
# Simétrica         A ^ B               Retorna os elementos da união de A com B
#                                       e que não pertencem à sua interseção
#                                       Equivale ao método .symmetric_difference()
print(A ^ B)    # {'N', 'I', 'T', 'J', 'É'}


# Pertence          valor in A          O valor está presente no conjunto A
print('X' in A)     # False
print('T' in A)     # True


# Não Pertence      valor not in A      O valor não está presente no conjunto A
print('X' not in A)     # True
print('T' not in A)     # False


# Neste quadro destacamos os métodos que equivalem a cada um dos operadores. A diferença entre
# eles é que os operadores se aplicam apenas a dois conjuntos por vez e os métodos podem ser usados com
# mais conjuntos em uma única operação.
