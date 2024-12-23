# Enunciado: Escreva um programa que leia um número inteiro N.
# Em seguida leia N números reais carregando-os em uma lista.
# Ao final exiba os elementos da lista na tela, sendo um em cada linha

N = int(input('Digite a quantidade: '))
L = []
for i in range(N):
    X = float(input(f' elemento {i}: '))
    L.append(X)
print('\nResultado:')
for valor in L:
    print(f' {valor}')
print('Fim do Programa')

# Digite a quantidade: 4
#  elemento 0: 3.1
#  elemento 1: 19.8
#  elemento 2: 7.35
#  elemento 3: 12.4
#
# Resultado:
#  3.1
#  19.8
#  7.35
#  12.4
# Fim do Programa


# Nesta solução 7.3 o comando for foi usado duas vezes. Na primeira, em combinação com a classe
# range, são lidos vários valores de entrada e cada um é adicionado à lista L. Terminada a fase de aquisição
# dos dados é feita a exibição com o segundo comando for.
