# Enunciado: Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
# de números inteiros aleatórios. Exiba a lista na tela.
# Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X for maior
# que zero. Para cada valor de X verifique se ele está ou não na lista gerada. Caso esteja é preciso exibir
# a quantidade de ocorrências.

from random import randint
# primeira parte - geração da lista
Lst = []
Qtde = int(input('Digite a quantidade: '))
for i in range(Qtde):
    a = randint(1, 20)
    Lst.append(a)
print('Lista gerada:')
print(f' {Lst}\n')

# segunda parte - pesquisa na lista
X = 1
while X > 0:
    X = int(input('Digite X: '))
    if X in Lst:
        print(f' há {Lst.count(X)} ocorrência(s) de {X} na lista')
    else:
        print(f' {X} não está na lista')
print('Fim do Programa')

# Digite a quantidade: 20
# Lista gerada:
#  [9, 10, 13, 18, 16, 20, 15, 12, 2, 14, 13, 17, 14, 20, 7, 20, 8, 4, 20, 12]
#
# Digite X: 9
#  há 1 ocorrência(s) de 9 na lista
# Digite X: 20
#  há 4 ocorrência(s) de 20 na lista
# Digite X: 3
#  3 não está na lista
# Digite X: 12
#  há 2 ocorrência(s) de 12 na lista
# Digite X: 0
#  0 não está na lista
# Fim do Programa


# Esta solução tem duas partes. Na primeira é feita a geração e a exibição da lista. Como o enunciado
# fala em gerar números inteiros aleatórios, foi usada a função randint() que pertence ao módulo Random,
# que faz parte da instalação padrão de Python. Os valores foram gerados na faixa de 1 a 20 quando escrevemos
# a = randint(1, 20), mas você pode mudar esses limites e ver como fica a geração da lista.

# Na segunda parte foi usado o operador in para saber se o valor de X está na lista e foi usado o método
# .count() para saber a quantidade de ocorrências.
