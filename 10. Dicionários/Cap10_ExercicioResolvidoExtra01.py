# Este é um comentário conjunto, válido para os exercícios resolvidos 10.3 e 10.4, os quais tem o mesmo enunciado,
# porém soluções distintas. Ambos usam a sigla como chave e a diferença relevante está na forma como foi
# estruturado o valor de cada elemento do dicionário. Essa diferença de estrutura implica em conhecermos
# dois aspectos da questão:
# • Como criar o elemento do dicionário;
# • Como usar o elemento do dicionário.

# Momento da criação - em 10.3 o valor é uma tupla;
# Isso implica que no momento da criação do elemento deverá ser usada a construção onde o lado direito
# da atribuição é uma tupla.
# UF[sigla] = (estado, capital, pib)

# Momento da criação - em 10.4 o valor é um dicionário aninhado.
# Isso implica que no momento da criação do elemento deverá ser usada a construção onde o lado direito
# da atribuição é um dicionário.
# dicItem = {'nome': estado, 'capital': capital, 'pib': pib}
# UF[sigla] = dicItem


# No que diz respeito ao uso do dicionário, em ambos utiliza-se o iterador for da forma abaixo:
# for sigla, dados in UF.items():

# Momento do uso - em 10.3 o valor é uma tupla;
# Neste caso, dados será uma tupla contendo 3 elementos e deverá ser usado com índices:
# print('({}) {:15} {:15} {:10.1f}'.format(
#     sigla,
#     dados[0],
#     dados[1],
#     dados[2] )

# Momento do uso - em 10.4 o valor é um dicionário aninhado;
# Neste caso, dados será um dicionário contendo 3 elementos e deverá ser usado com chave:
# print('({}) {:15} {:15} {:10.1f}'.format(
#     sigla,
#     dados['nome'],
#     dados['capital'],
#     dados['pib'] )


# Esteja atento a esses pontos e a cada novo problema escolha a estratégia que você considerar mais
# adequada à situação.
