# Por fim, tuplas e listas são totalmente intercambiáveis, ou seja, é possível realizar conversões entre
# objetos dessas duas classes. Veja o exemplo a seguir:

T = (3.6, 120, 'texto')
print(type(T))      # <class 'tuple'>

T = list(T)         # converte T para lista e armazena no próprio identificador T
print(type(T))      # <class 'list'>
T[0] = 19.25        # alterando um elemento de T. Não ocorre erro porque é lista
print(T)            # [19.25, 120, 'texto']

T = tuple(T)        # reconvertendo a lista T para tupla
print(type(T))      # <class 'tuple'>
print(T)            # (19.25, 120, 'texto')


# Neste exemplo convertemos a tupla T para lista, alteramos um de seus valores e retornamos de lista para tupla.
# Isso é algo que sempre pode ser feito em nossos programas, mas antes de se fazê-lo pense se é mesmo necessário.
# Fazemos esse aviso porque, se muitas conversões entre tuplas e listas precisarem ser feitas, considere
# usar uma lista de uma vez por todas e não gastar processamento com as conversões em si.
