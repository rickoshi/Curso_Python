# ELIMINAÇÃO DE ELEMENTOS USANDO A FUNÇÃO del
# Muitas vezes há necessidade de eliminar um ou mais elementos de uma lista.
# Um dos modos de fazer isso é usando a função del.
# Para usá-la é preciso saber o índice do elemento você quer eliminar e escrevê-la no formato mostrado a seguir.

A = [10, 12, 14, 16]
print(A)        # [10, 12, 14, 16]
del A[0]
print(A)        # [12, 14, 16]
