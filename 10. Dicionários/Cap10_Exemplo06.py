# ITERAÇÕES COM DICIONÁRIOS
# O uso mais frequente de dicionários é como iterador em um comando for. Há três casos típicos.

# CASO 2 – ITERAÇÃO SOBRE OS VALORES
# Há situações nos programas em que não estamos interessados nas chaves dos elementos do dicionário.
# Ao invés disso estamos interessados apenas nos valores.

Cores = {1: 'azul', 2: 'verde', 3: 'amarelo', 4: 'vermelho'}
print('Exibição do dicionário - Caso 2')
for cor in Cores.values():
    print(f'  {cor}')
print('Fim do programa')

# Exibição do dicionário - Caso 2
#   azul
#   verde
#   amarelo
#   vermelho
# Fim do programa


# Para casos assim podemos usar o método .values() para iterar diretamente sobre os valores. Neste
# exemplo o objeto cor recebe diretamente os nomes das cores e os utiliza no processamento
