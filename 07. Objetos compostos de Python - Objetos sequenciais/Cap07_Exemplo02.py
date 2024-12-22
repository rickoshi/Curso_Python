# Vamos explorar um pouco mais a interação com a lista.
# No exemplo a seguir, criamos a lista com 10 elementos; exibimos o tipo de L;
# exibimos individualmente alguns elementos usando o índice;
# exibimos o tamanho da lista com o uso da função len(); alteramos o primeiro valor da lista;
# e por fim exibimos a lista inteira para conferir se a alteração do primeiro item de fato ocorreu.

L = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
print(type(L))          # <class 'list'>
print(L[0])             # 36
print(type(L[0]))       # <class 'int'>
print(L[9])             # 31
print(len(L))           # 10
L[0] = 999
print(L)                # [999, 25, 21, 48, 17, 9, 16, 23, 29, 31]

# Nesta lista todos os elementos são da classe int, de modo que dizemos que essa é uma lista homogênea.
# É comum que todos os elementos da lista sejam da mesma classe e quando isso ocorre dizemos que
# a lista é homogênea. Porém isso não é obrigatório, ou seja, uma lista pode conter elementos classes
# diferentes e aí dizemos que a lista é heterogênea
