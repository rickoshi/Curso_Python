# Enunciado: Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
# de inteiros aleatórios. Exiba a lista na tela. Em seguida elimine valores que estiverem repetidos,
# deixando apenas uma ocorrência de cada. Exiba a nova lista sem repetidos e o seu tamanho.

from random import randint
Qtde = int(input('Digite a quantidade: '))
Lista = []
for i in range(Qtde):
    Lista.append(randint(1, 50))
print('\nLista gerada:')
print(Lista)
conjunto = set(Lista)   # converte a lista em conjunto
Lista = set(conjunto)   # retorna o conjunto para lista
print('\nLista com valores não repetidos:')
print(Lista)
print(f'A nova lista tem {len(conjunto)} elementos')
print('Fim do Programa')

# Digite a quantidade: 20
#
# Lista gerada:
# [26, 16, 8, 26, 2, 41, 24, 40, 48, 11, 50, 5, 8, 3, 50, 18, 14, 4, 31, 49]
#
# Lista com valores não repetidos:
# {2, 3, 4, 5, 8, 11, 14, 16, 18, 24, 26, 31, 40, 41, 48, 49, 50}
# A nova lista tem 17 elementos
# Fim do Programa
