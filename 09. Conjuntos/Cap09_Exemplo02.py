# Podemos criar um conjunto não vazio usando o construtor da classe.
# Neste caso o construtor deve receber como parâmetro iterável, podendo ser string, tupla, lista, conjunto ou
# dicionário. O exemplo a seguir ilustra esses vários casos

# Criação do conjunto a partir de string
texto = 'texto qualquer'
c = set(texto)
print(c)        # {'r', 't', 'l', ' ', 'q', 'e', 'u', 'a', 'x', 'o'}
# observe que não há caracteres repetidos no conjunto

# Criação do conjunto a partir de tupla
tupla = (14, 26, 33, 45, 50)
c = set(tupla)
print(c)        # {33, 45, 14, 50, 26}

# Criação do conjunto a partir de lista
lista = (26, 15, 49, 65, 49)
c = set(lista)
print(c)        # {65, 49, 26, 15}

# Criação do conjunto a partir de outro conjunto
c2 = set(c)
print(c2)       # {65, 49, 26, 15}

# Criação do conjunto a partir de um dicionário
dicionario = {'1235': 49, '1476': 32, '1329': 36}
c = set(dicionario)
print(c)        # {'1476', '1329', '1235'}
