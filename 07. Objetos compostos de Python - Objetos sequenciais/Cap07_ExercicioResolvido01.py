# Enunciado: Escreva um programa que leia três números inteiros: o primeiro termo P, a razão R e a quantidade Q
# de termos de uma progressão aritmética. O programa deve calcular os Q termos da progressão
# colocando-os em uma lista e no final exibi-la na tela.
# obs: esse problema já foi abordado, sem o uso de listas, no exercício resolvido 5.3.

P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Q = int(input("Digite a qtde de termos: "))
Termos = [P]        # cria a lista já com o primeiro termo
i = 0
while i < Q-1:          # vai até Q-1 porque o primeiro termo já esta na lista
    P = P + R           # calcula o próximo termo
    Termos.append(P)    # acrescenta o termo à lista
    i += 1
print('Lista resultante')
print(Termos)
print('Fim do Programa')

# Digite o primeiro termo: 4
# Digite a razão: 7
# Digite a qtde de termos: 12
# Lista resultante
# [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81]
# Fim do Programa


# Nesta solução a lista Termos é inicialmente criada contendo o primeiro termo.
# A cada repetição do laço while um novo termo é calculado e acrescentado na lista.
# Para que a lista termine com a quantidade correta Q de termos é preciso tomar um cuidado.
# Como o primeiro termo é pré-colocado na lista fora do laço, na condição usada no while foi preciso descontar 1 de Q.
# Se isso não fosse feito a lista ficaria no final com um termo a mais do que foi pedido.
