# Em Python é possível fazer atribuição múltipla
A = B = 10          # cria dois identificadores que apontam para um objeto int
C = D = 3.5         # cria dois identificadores que apontam para um objeto float
E = F = 'python'    # cria dois identificadores que apontam para um objeto string

# Ambos os objetos recebem os mesmos valores e identificadores
print((A, B), id(A), id(B))     # (10, 10) 140730962090712 140730962090712
print((C, D), id(C), id(D))     # (3.5, 3.5) 1479794273392 1479794273392
print((E, F), id(E), id(F))     # ('python', 'python') 1479794801712 1479794801712

# Entretanto para as classes mutáveis, a atribuição múltipla é um pouco diferente
G = H = [0, 1]              # Cria dois identificadores que apontam para um objeto list
print(G, H, id(G), id(H))   # [0, 1] [0, 1] 2252285008064 2252285008064
G[0] = 30                   # Alteração do conteúdo apenas do objeto G
print(G, H, id(G), id(H))   # [30, 1] [30, 1] 2252285008064 2252285008064
# Como a classe list é mutável e os dois objetos se referem à mesma lista, quando ocorrer
# alteração em uma delas, essa alteração vai se refletir na outra.

# Outra forma de atribuição múltipla:
U, V = 10, 15
X, Y, Z = 12, 7.5, 8.43
# Temos dois ou mais identificadores do lado esquerdo e o mesmo número de valores do lado direito
# Em comandos assim o Python vai fazer a atribuição conforme a posição

print(U, type(U), V, type(V))               # 10 <class 'int'> 15 <class 'int'>
print(X, type(X), Y, type(Y), Z, type(Z))   # 12 <class 'int'> 7.5 <class 'float'> 8.43 <class 'float'>
