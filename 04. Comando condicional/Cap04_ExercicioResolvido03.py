# Enunciado: Altere o programa anterior de modo que ele continue exibindo o menor dos dois valores lidos.
# Porém, quando forem iguais o programa deve exibir o valor junto com o texto "Os dois números são iguais".

A = int(input('Digite A: '))
B = int(input('Digite B: '))
if A == B:
    print(f'Os dois números são iguais e valem {A}')
else:
    if A < B:
        print(f'O menor número é {A}')
    else:
        print(f'O menor número é {B}')
print('Fim do Programa')

# primeira execução
# Digite A: 6
# Digite B: 6
# Os dois números são iguais e valem 6
# Fim do Programa

# segunda execução
# Digite A: 10
# Digite B: 12
# O menor número é 10
# Fim do Programa

# terceira execução
# Digite A: 35
# Digite B: 18
# O menor número é 18
# Fim do Programa


# O código também pode ser reescrito usando a parte elif do comnado condicional
# A = int(input('Digite A: '))
# B = int(input('Digite B: '))
# if A == B: # A e B são iguais
#     print(f'Os dois números são iguais e valem {A}')
# elif A < B: # A é menor
#     print(f'O menor número é {A}')
# else: # B é menor
#     print(f'O menor número é {B}')
# print('Fim do Programa')
