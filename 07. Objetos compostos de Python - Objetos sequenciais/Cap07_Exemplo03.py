# OPERAÇÕES COM LISTAS
# As listas de Python oferecem ao programador uma gama muito grande de operações que podem ser realizadas.
# Essas operações podem ser feitas tanto a partir de funções de Python externas à classe list
# quanto a partir dos métodos disponíveis na própria classe list.

# CRIAÇÃO DE UMA LISTA DO ZERO
# Por ser muito frequente, a primeira operação que precisamos aprender é como criar uma lista vazia e incluir elementos.
# O exemplo a seguir mostra que para criar a lista basta executar a atribuição L = [], que pode
# ser lida como "objeto recebe par de colchetes". Usando a função type() conferimos que L foi criado e que
# ele é da classe list. Em seguida, usando o método .append() fizemos a inclusão de dois números reais
# e exibimos a lista com print(). O método .append()sempre faz a inclusão de objetos no final da lista.

L = []
print(type(L))          # <class 'list'>
L.append(3.88)
L.append(17.5)
print(L)                # [3.88, 17.5]
print(type(L[0]))       # <class 'float'>

