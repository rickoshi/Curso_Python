# RELAÇÃO ENTRE HASH E CONJUNTOS
# Existe uma relação entre o número hash de um objeto e os conjuntos. Em Python, apenas objetos de
# classes hashable podem pertencer a conjuntos. Além disso, a regra dos elementos não repetidos em
# conjuntos é imposta através desse número hash. Por consequência, valores numéricos inteiros e reais como
# mencionado acima (o caso 26 e 26.0) não podem coexistir em um conjunto. Isso é mostrado neste exemplo:

c = {26, 26.0}
print(c)    # {26}
