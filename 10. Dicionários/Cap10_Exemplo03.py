# Ao usar a construção de dicionário vazio e adicionar elementos abaixo podem acontecer duas coisas:

# dicionario[chave] = valor

# a) se a chave não existe no dicionário, então o elemento é criado;
# b) se a chave já existe no dicionário, então o elemento é alterado;

D = {}              # cria o dicionário vazio
D['a'] = 120        # insere novo elemento com chave 'a'
print(D)            # {'a': 120}

D['a'] = 250        # altera o elemento com chave 'a'
print(D)            # {'a': 250}

D['b'] = 521
print(D)            # {'a': 250, 'b': 521}


# É possível fazer operações com as chaves que existem e os valores numéricos
x = D['a'] + D['b']
print(x)            # 771

D['a'] += 100
print(D)            # {'a': 350, 'b': 521}


# É possível acessar as chaves utilizando variáveis ao invés do próprio valor
chave = 'a'
print(D[chave])     # 350

chave = 'b'
print(D[chave])     # 521

chave = 'c'
D[chave] = 0
print(D)            # {'a': 350, 'b': 521, 'c': 0}


# É possível utilizar outros valores para as chaves dos dicionários
M = {}
print(type(M))      # <class 'dict'>

M[110] = 45.6
print(M)            # {110: 45.6}

M[9.2] = 'xpto'
print(M)            # {110: 45.6, 9.2: 'xpto'}

M[(1, 0, 5)] = 281.9
print(M)            # {110: 45.6, 9.2: 'xpto', (1, 0, 5): 281.9}
