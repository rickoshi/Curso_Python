# Enunciado: Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois.
# Se ambos forem iguais, mostre qualquer um deles.

A = int(input('Digite A: '))
B = int(input('Digite B: '))
if A <= B:
    print(f'O menor número é {A}')
else:
    print(f'O menor número é {B}')
print('Fim do Programa')

# primeira execução
# Digite A: 23
# Digite B: 78
# O menor número é 23
# Fim do Programa

# segunda execução
# Digite A: 58
# Digite B: 12
# O menor número é 12
# Fim do Programa
