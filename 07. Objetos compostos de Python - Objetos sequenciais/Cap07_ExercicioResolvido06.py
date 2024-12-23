# Enunciado: Escreva um programa que permaneça em laço lendo números inteiros. O laço termina quando for
# digitado 0 (zero). Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que
# ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. Se um valor repetido for digitado,
# o programa deve exibir uma mensagem na tela.
# Ao final exiba a lista e a quantidade de elementos que ela contém.

LstValores = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    if valor not in LstValores:
        LstValores.append(valor)
    else:
        print(f' erro! o valor {valor} já está na lista')
    valor = int(input('Digite um inteiro: '))
print('\nResultado')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos')
print('Fim do Programa')

# Digite um inteiro: 23
# Digite um inteiro: 14
# Digite um inteiro: 23
#  erro! o valor 23 já está na lista
# Digite um inteiro: 19
# Digite um inteiro: 0
#
# Resultado
# [23, 14, 19]
# A lista contém 3 elementos
# Fim do Programa


# Neste problema queremos criar uma lista sem valores repetidos. Para implementar a solução é preciso
# acrescentar uma verificação dentro do laço usando o operador not in, conforme mostrado acima. Se o
# valor não está na lista é acrescentado e se já está a mensagem de erro é exibida.
