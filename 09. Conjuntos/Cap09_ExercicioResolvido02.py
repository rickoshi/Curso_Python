# Enunciado: Escreva um programa que leia do teclado dois conjuntos de números inteiros digitados pelo usuário.
# Exiba na tela a união e a interseção desses conjuntos

Msg = 'Digite Valor: '
print('Dados do primeiro conjunto')
C1 = set()          # cria o primeiro conjunto vazio
x = int(input(Msg))
while x != 0:
    C1.add(x)       # acrescenta o novo elemento, se ainda não estiver no conjunto
    x = int(input(Msg))
print('Dados do segundo conjunto')
C2 = set()          # cria o segundo conjunto vazio
x = int(input(Msg))
while x != 0:
    C2.add(x)       # acrescenta o novo elemento, se ainda não estiver no conjunto
    x = int(input(Msg))
print(f'\nConjunto 1: {C1}')
print(f'Conjunto 2: {C2}')
print('\nUnião de C1 e C2')
print(C1 | C2)
print('\nInterseção de C1 e C2')
print(C1 & C2)
print('\nFim do Programa')

# Dados do primeiro conjunto
# Digite Valor: 16
# Digite Valor: 8
# Digite Valor: 44
# Digite Valor: 0
# Dados do segundo conjunto
# Digite Valor: 12
# Digite Valor: 14
# Digite Valor: 16
# Digite Valor: 10
# Digite Valor: 8
# Digite Valor: 0
#
# Conjunto 1: {16, 8, 44}
# Conjunto 2: {8, 10, 12, 14, 16}
#
# União de C1 e C2
# {8, 10, 44, 12, 14, 16}
#
# Interseção de C1 e C2
# {16, 8}
#
# Fim do Programa
