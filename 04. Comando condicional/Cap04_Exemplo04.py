# NEGAÇÕES E CONDIÇÕES COMPOSTAS
# Muitas vezes é preciso negar uma condição simples ou combinar duas ou mais condições simples em uma condição composta.
# Para isso são usados os operadores lógicos.
# Existem três operadores lógicos em Python:

# Operador      O que ele faz           Descrição
# not           Negação                 Nega a condição à qual é aplicado
# and           Conjunção (E)           Resulta verdadeiro se forem verdadeiras as duas condições às quais é aplicado
# or            Disjunção (OU)          Resulta verdadeiro se for verdadeira pelo menos uma das duas condições

# Cada um desses operadores é regido por uma Tabela Verdade que define seus resultados em função das entradas

# Observação:
# A linguagem Python não possui o operador lógico xor (ou exclusivo) que costuma estar disponível em outras linguagens.
# Se você precisar usar esse operador deverá usar a expressão equivalente:
# C1 xor C2 = (not C1 and C2 or C1 and not C2)


# CONDIÇÕES COMPOSTAS MISTAS
# Esse tipo de condição ocorre quando em uma única condição composta for preciso usar not, and e or de forma combinada.
# Quando isso ocorre é preciso prestar atenção à precedência com que esses operadores são considerados.
# Existe uma ordem de prioridade a ser respeitada. Essa prioridade segue a seguinte ordem:
# not primeiro; and em seguida; or por último.
# É possível usar parênteses para alterar a ordem de prioridade na avaliação dessas expressões.
# Uma vez inseridos, os parênteses modificam as prioridades e estabelecem a ordem de avaliação

A = 15
B = 9
C = 9
print(B == C or A < B and A < C)        # True
print((B == C or A < B) and A < C)      # False
