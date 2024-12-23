# CÓPIA DE UMA LISTA USANDO FATIAMENTO
# Copiar uma lista é uma operação frequentemente necessária. Para programadores desavisados e
# iniciantes essa operação pode ser uma armadilha. Veja as linhas a seguir e reflita: ao fazer B = A a
# lista A foi copiada na lista B?

A = [10, 12, 14, 16]
B = A

# A resposta é não, a lista B não é uma cópia de A. Depois de fazer B = A mandamos
# exibir o id dos dois objetos e constatemos que eles são iguais.

print(id(A))        # 1873000649088
print(id(B))        # 1873000649088

B[0] = 99
print(B)            # [99, 12, 14, 16]
print(A)            # [99, 12, 14, 16]


# Isso acontece porque a classe list de Python é mutável.
# Quando fizemos B = A neste exemplo o que o Python fez foi criar o objeto B em memória e copiar o id de A para B.
# Com isso, na prática, só existe uma lista em memória e os dois objetos, A e B, apontam para ela.
# Por consequência qualquer alteração de dados que for feita em B também refletirá em A e vice-versa.
# No exemplo alteramos o primeiro elemento de B para 99 e mostramos que A também ficou alterado.
# Para quem está aprendendo Python isso pode ser estranho e incômodo no início, então fique atento e
# não caia nessa armadilha. Agora a pergunta: se não dá para fazer B = A, como fazer então?

# A resposta é simples: use o fatiamento para copiar todos os elementos para uma nova lista:

A = [10, 12, 14, 16]
B = A[:]

print(id(A))        # 2374410614720
print(id(B))        # 2374410610816

B[0] = 99
print(B)            # [99, 12, 14, 16]
print(A)            # [10, 12, 14, 16]

# Nessa nova versão foi usado o fatiamento no formato Destino = Origem[:] que faz com que
# a lista Destino seja uma cópia integral e com id próprio da lista Origem.


# Aviso e Dica
# O aviso: cuidado com cópias de listas em seus programas.
# Se elas forem pequenas, certamente não haverá problemas.
# Porém, se suas listas forem grandes, com muitos de milhares de elementos,
# fazer cópias e mais cópias pode levar a uma
# lentidão indesejada na execução do seu programa.
# Assim, a dica é: só faça cópia de uma lista muito grande quando isso for
# absolutamente necessário e saiba que isso é necessário em poucas ocasiões.
