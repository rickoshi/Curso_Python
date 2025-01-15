# ITERAÇÕES COM DICIONÁRIOS
# O uso mais frequente de dicionários é como iterador em um comando for. Há três casos típicos.

# CASO – ITERAÇÃO CONJUNTA CHAVE-VALOR
# Esta terceira situação também é muito frequente. Usando o método .items() podemos iterar
# simultaneamente com as chaves e os valores.

Cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário - Caso 3')
for numero, nome in Cores.items():
    print(f'  n° da cor = {numero} - nome da cor = {nome}')
print('Fim do programa')

# Exibição do dicionário - Caso 3
#   n° da cor = 1 - nome da cor = azul
#   n° da cor = 2 - nome da cor = verde
#   n° da cor = 3 - nome da cor = amarelo
#   n° da cor = 4 - nome da cor = vermelho
# Fim do programa


# Nesta solução aparecem dois objetos usados no controle do comando for desta forma:

# for numero, nome in Cores.items():

# Mas cuidado, não interprete errado. Você não está vendo "dois objetos" como controle do comando
# for. De fato, o Python é cheio de sutilezas e passo-a-passo você precisa aprender os conceitos e assim vai
# entender tais sutilezas.


# Na prática o par (numero, nome) assim colocado no for é interpretado pelo Python como sendo uma
# tupla que recebe a tupla retornada pelo método .items(). Portanto o conceito é esse: se o retorno do
# método .items() é uma tupla, então o objeto que a recebe também será uma tupla.
# Assim, a linha acima é o mesmo que escrever a linha a seguir:

# for (numero, nome) in Cores.items():

# ou ainda deste modo

# for tupla in Cores.items():
