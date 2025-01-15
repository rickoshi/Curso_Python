# ITERAÇÕES COM DICIONÁRIOS
# O uso mais frequente de dicionários é como iterador em um comando for. Há três casos típicos.

# CASO – ITERAÇÃO CONJUNTA CHAVE-VALOR
# Esta terceira situação também é muito frequente. Usando o método .items() podemos iterar
# simultaneamente com as chaves e os valores.

Cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário - Caso 3')
for tupla in Cores.items():
    print(f'  {tupla}')
print('Fim do programa')

# Exibição do dicionário - Caso 3
#   (1, 'azul')
#   (2, 'verde')
#   (3, 'amarelo')
#   (4, 'vermelho')
# Fim do programa


# O par (numero, nome) é interpretado pelo Python como sendo uma tupla que recebe a
# tupla retornada pelo método .items(). Portanto o conceito é esse: se o retorno do
# método .items() é uma tupla, então o objeto que a recebe também será uma tupla.

# Assim, as linhas a seguir fazem a mesma coisa, porém são escritas de forma diferente:

# for numero, nome in Cores.items():
# for (numero, nome) in Cores.items():
# for tupla in Cores.items():


# Repare no uso do identificador 'tupla' no exemplo a seguir, bem como na forma como foi usado no print.

Cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário - Caso 3')
for tupla in Cores.items():         # veja o uso do identificador 'tupla'
    print(f'  n° da cor = {tupla[0]} - nome da cor = {tupla[1]}')   # e atenção aqui
print('Fim do programa')

# Exibição do dicionário - Caso 3
#   n° da cor = 1 - nome da cor = azul
#   n° da cor = 2 - nome da cor = verde
#   n° da cor = 3 - nome da cor = amarelo
#   n° da cor = 4 - nome da cor = vermelho
# Fim do programa
