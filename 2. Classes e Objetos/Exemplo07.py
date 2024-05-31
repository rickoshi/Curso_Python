# Objeto Imutável
# A alteração de conteúdo implica na alteração do id
obj1 = 8
print(id(obj1))     # 140714827782808
obj1 = 12
print(id(obj1))     # 140714827782936

# Objeto Mutável
# A alteração de conteúdo ocorre sem a alteração do id
# L é uma lista: uma coleção de objetos
L = [44, 17, 26, 35, 20]
print(type(L))      # <class 'list'>
print(L)            # [44, 17, 26, 35, 20]
print(len(L))       # 5
print(id(L))        # 2816931582336
print(L[0])         # 44
print(L[1])         # 17

L[0] = 12
print(L)            # [12, 17, 26, 35, 20]
print(id(L))        # 2816931582336

'''
Classes de objetos Imutáveis
int, float, complex, bool
string, tuple, range, frozenset, bytes

Classes de objetos Mutáveis
lis, set, dict, bytearray
'''
