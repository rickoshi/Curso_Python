# ESTRUTURA DO DICIONÁRIO
# Dicionários em Python são coleções de pares chave-valor. E guardam certa semelhança com as listas.

# Imagine que você precisa elaborar uma aplicação que contenha dados de estados do Brasil: (sigla,
# nome, capital, PIB estadual em 2021). Você pode criar uma lista onde cada elemento seja uma tupla
# contendo os dados necessários. Essa lista teria uma aparência como mostrada no lado direito da imagem.
# Por ser um objeto sequencial, a lista exige o uso do índice numérico – 0, 1, 2, 3, etc – para acesso individual
# aos dados dos Estados.
# Neste caso, o dicionário permite fazer algo mais bem elaborado para essa aplicação. O lado esquerdo
# da imagem mostra que ao adotar um dicionário podemos usar a sigla do Estado como chave de acesso e os
# dados associados são o valor.
# Daí decorre a ideia da associação chave-valor mencionada.

# A classe dict de Python é o elemento da linguagem que permite esse tipo de construção.
# Apresentado dessa forma pode parecer que os dicionários são melhores que as listas. Não é verdade.
# Na prática, ambos tem muita importância na linguagem Python. Há situações mais adequadas para listas e
# outras mais adequadas para dicionários e um fato é certo: os dicionários e as listas estão entre as classes de
# objetos mais flexíveis e poderosos de Python.

# Dicionários e listas se assemelham algumas características:
# • são mutáveis;
# • são dinâmicos, ou seja, podem crescer e diminuir conforme necessário;
# • podem ser aninhados, ou seja, uma lista pode conter outra lista; um dicionário pode conter outro
# dicionário; um dicionário pode conter uma lista e vice-versa.

# Dicionários e listas diferem na forma como os elementos são acessados:
# • Os elementos da lista são acessados pela sua posição na lista, via indexação.
# • Os elementos do dicionário são acessados por meio de chaves

# Quaisquer objetos de classes imutáveis podem ser usados como chave de um elemento de um
# dicionário, exceto uma tupla que contenha uma ou mais listas.

# Valor dos elementos de um dicionário
# O valor de um elemento de dicionário pode ser qualquer objeto


# CRIAÇÃO DE UM DICIONÁRIO
# A sintaxe para uso dos dicionários se assemelha muito à sintaxe usada para as listas, com a diferença
# de que no lugar do índice utiliza-se a chave. Veja o exemplo a seguir onde criamos um dicionário com três
# elementos, usando como chave um string e como valor outro string.

UF = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais'}
print(type(UF))     # <class 'dict'>
print(UF)           # {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais'}

# A sintaxe para criar um dicionário pré-carregado com dados envolve a especificação do elemento
# através do par chave-valor separados pelo caractere ':' (dois pontos). E os vários elementos devem estar
# separados por vírgula.

# dicionario = {chave1: valor1, chave2: valor2, ...}
