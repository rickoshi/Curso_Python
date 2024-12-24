# A função print() realiza operações de saída de dados
# Tem a seguinte estrutura de parâmetros:
# print(*objects, sep=' ', end='\n', file=None, flush=False)

# onde:
# *objects é o conjunto de objetos cujo conteúdo será exibido;
# sep       separador a ser usado quando *objects contiver mais de um objeto. Valor padrão é um branco;
# end       contém o caractere a ser enviado para a saída no final. Seu valor padrão é \n (pulo de linha);
# file      define o arquivo de saída. Seu valor padrão é None, indicando que a saída é a tela;
# flush     se for True indica que o buffer de saída deve ser esvaziado. Seu valor padrão é False
# O único parâmetro obrigatório é *objects. Os demais são opcionais e têm valor padrão.

print('Esta é uma mensagem exemplo')    # Esta é uma mensagem exemplo

X = 26
print(X)        # 26
Y = 58
print(Y)        # 58
print(X, Y)     # 26 58

print('Valor de X =', X)    # Valor de X = 26

# Produzindo uma saída formatada. Esse tipo de saída permite controlar detalhes da exibição dos dados.
print('Valores: X = {0} e Y = {1}'.format(X, Y))    # Valores: X = 26 e Y = 58
print('Valores: Y = {0} e X = {1}'.format(Y, X))    # Valores: Y = 58 e X = 26
print('Valores: X = {1} e Y = {0}'.format(Y, X))    # Valores: X = 26 e Y = 58
