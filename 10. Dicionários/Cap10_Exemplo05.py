# ITERAÇÕES COM DICIONÁRIOS
# O uso mais frequente de dicionários é como iterador em um comando for. Há três casos típicos.

# CASO 1 – ITERAÇÃO SOBRE AS CHAVES
# O exemplo a seguir mostra a iteração sobre as chaves.

Cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário - Caso 1')
for x in Cores.keys():              # Cores.keys() foi usado explicitamente
    print(f'  {x} - {Cores[x]}')    # Cores[x] dá acesso ao valor associado a x
print('Fim do programa')

# Exibição do dicionário - Caso 1
#   1 - azul
#   2 - verde
#   3 - amarelo
#   4 - vermelho
# Fim do programa

Cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário - Caso 1')
for x in Cores:                     # Cores.keys() foi usado implicitamente
    print(f'  {x} - {Cores[x]}')
print('Fim do programa')

# Exibição do dicionário - Caso 1
#   1 - azul
#   2 - verde
#   3 - amarelo
#   4 - vermelho
# Fim do programa


# Este exemplo mostra duas versões do programa com uma única diferença na linha do comando for.
# O objeto x é o objeto de controle do comando for e a cada iteração ele recebe a chave de um elemento
# contido na lista. O conjunto de chaves é fornecido pelo método .keys() e esse método é padrão (default)
# no dicionário de modo que escrever uma das alternativas abaixo dá o mesmo resultado.

# for x in Cores.keys():
# for x in Cores:

# Além disso, uma vez que x contém a chave de um elemento é possível acessar seu valor com:

# Cores[x]

# E isso foi usado no momento de exibir o resultado na tela.
