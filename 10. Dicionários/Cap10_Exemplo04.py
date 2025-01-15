# MÉTODOS DA CLASSE dict
# A classe dict tem um conjunto de métodos que os programadores devem conhecer. Eles são
# apresentados no quadro a seguir:

D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão'}
print(len(D))   # 5
print(D)        # {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}

# Método                        Descrição
# .clear()                      Remove todos os elementos do dicionário.
D.clear()
print(D)        # {}
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão'}
print(D)        # {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão'}


# .copy()                       Retorna uma cópia do dicionário.
A = D.copy()
print(A)        # {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão'}
print(id(D))    # 2897270794880
print(id(A))    # 2897270794432


# .get(key [,default])          Retorna o valor associado com a chave key passada como parâmetro. Caso a
#                               chave não esteja presente retorna o segundo parâmetro default. O segundo
#                               parâmetro é opcional e na sua ausência o retorno será None.
X = A.get(134)
print(X)        # Arroz
X = A.get(12, 'Chave não existe')
print(X)        # Chave não existe


# .fromkeys(iteravel [,v])      Cria um novo dicionário usando os elementos do objeto iteravel como
#                               chave. Se o segundo parâmetro for fornecido será usado como valor para todos
#                               os elementos do novo dicionário.
codigos = (111, 139, 143, 157)
Y = A.fromkeys(codigos)
print(Y)        # {111: None, 139: None, 143: None, 157: None}
Y = A.fromkeys(codigos, 'algo')
print(Y)        # {111: 'algo', 139: 'algo', 143: 'algo', 157: 'algo'}

del A           # Deleta A, não irá mais existir em memória
A = {}.fromkeys(codigos, '')
print(A)        # {111: '', 139: '', 143: '', 157: ''}
A[111] = 'Vinagre'
print(A)        # {111: 'Vinagre', 139: '', 143: '', 157: ''}


# .pop(key [,default])          Remove a chave key do dicionário e retorna o valor a ela associado. Caso a
#                               chave não esteja presente retorna o segundo parâmetro default.
#                               Se key não existe e default não foi especificado gera a exceção KeyError.
print(D)        # {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão'}
X = D.pop(120)
print(X)        # Queijo
print(D)        # {134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão'}
X = D.pop(117)
print(X)        # Farinha
print(D)        # {134: 'Arroz', 125: 'Açúcar', 133: 'Macarrão'}
X = D.pop(30, 'Chave não existe')
print(X)        # Chave não existe
print(D)        # {134: 'Arroz', 125: 'Açúcar', 133: 'Macarrão'}


# .popitem()                    Remove um elemento do dicionário, retornando-o na forma de um par
#                               chave-valor. Os elementos são retornados na ordem de uma pilha LIFO, ou seja,
#                               o último elemento a entrar é o primeiro a ser retirado.
#                               Se o dicionário estiver vazio gera a exceção KeyError
print(D)        # {134: 'Arroz', 125: 'Açúcar', 133: 'Macarrão'}
X = D.popitem()
print(X)        # (133, 'Macarrão')
print(type(X))  # <class 'tuple'>
print(D)        # {134: 'Arroz', 125: 'Açúcar'}
X = D.popitem()
print(X)        # (125, 'Açúcar')
print(D)        # {134: 'Arroz'}


# .setdefault(key [,d])         Se a chave key está no dicionário, retorna o seu valor. Senão, insere key com o
#                               valor default e retorna default. Por padrão default é o valor None.
#                               Este método representa uma forma alternativa de inicializar um dicionário
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão'}
R = D.setdefault(144, 'Feijão')
print(R)        # Feijão
print(D)        # {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão', 144: 'Feijão'}
R = D.setdefault(117, 'Feijão')
print(R)        # Farinha
print(D)        # {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão', 144: 'Feijão'}


# .update(origem)               Atualiza o dicionário a partir dos itens contidos no parâmetro origem. Se
#                               algum item de origem não estiver presente então será incluído; se estiver será
#                               atualizado.
D.update( ( (177, 'Cebola'), (217, 'Maçã'), (185, 'Abacate') ) )
print(D)        # {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão', 144: 'Feijão',
#                  177: 'Cebola', 217: 'Maçã', 185: 'Abacate'}
D.update(((177, 'Tomate'), (217, 'Banana'), (185, 'Melão')))
print(D)        # {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açúcar', 133: 'Macarrão', 144: 'Feijão',
#                  177: 'Tomate', 217: 'Banana', 185: 'Melão'}


# .keys()                       Retorna uma coleção com todas as chaves dos elementos contidos no
#                               dicionário.
Ch = D.keys()
print(type(Ch))     # <class 'dict_keys'>
print(Ch)           # dict_keys([120, 134, 117, 125, 133, 144, 177, 217, 185])


# .values()                     Retorna uma coleção com todos os valores dos elementos contidos no
#                               dicionário.
Vl = D.values()
print(type(Vl))     # <class 'dict_values'>
print(Vl)           # dict_values(['Queijo', 'Arroz', 'Farinha', 'Açúcar', 'Macarrão', 'Feijão',
#                     'Tomate', 'Banana', 'Melão'])


# .items()                      Retorna o conjunto de elementos do dicionário na forma de tuplas contendo o
#                               par chave-valor de cada um. Muito útil para usar em iterações com o dicionário.
It = D.items()
print(type(It))     # <class 'dict_items'>
print(It)           # dict_items([(120, 'Queijo'), (134, 'Arroz'), (117, 'Farinha'), (125, 'Açúcar'),
#                     (133, 'Macarrão'), (144, 'Feijão'), (177, 'Tomate'), (217, 'Banana'), (185, 'Melão')])

for k in D.items():
    print(k)

# (120, 'Queijo')
# (134, 'Arroz')
# (117, 'Farinha')
# (125, 'Açúcar')
# (133, 'Macarrão')
# (144, 'Feijão')
# (177, 'Tomate')
# (217, 'Banana')
# (185, 'Melão')
