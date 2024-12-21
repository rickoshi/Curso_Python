# Enunciado: Escreva um programa que mostre na tela a tabuada do número inteiro N que deve ser lido do teclado.

N = int(input('Digite N: '))
cont = 1
while cont <= 10:
    R = cont * N
    print(f'{cont} x {N} = {R}')
    cont = cont + 1
print('Fim do Programa')

# Digite N: 3
# 1 x 3 = 3
# 2 x 3 = 6
# 3 x 3 = 9
# 4 x 3 = 12
# 5 x 3 = 15
# 6 x 3 = 18
# 7 x 3 = 21
# 8 x 3 = 24
# 9 x 3 = 27
# 10 x 3 = 30
# Fim do Programa


# Neste exercício temos novamente o controle do laço feito com o uso de um contador.
# O objeto de controle do laço é o cont, inicializado com 1 e que é incrementado a cada repetição até que assuma um
# valor maior que 10. Para cada repetição é feito o cálculo do resultado da linha da tabuada e sua exibição.
