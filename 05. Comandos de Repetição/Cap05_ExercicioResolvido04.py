# Enunciado: Escreva um programa que leia do teclado um número inteiro D.
# Esse número deve ser obrigatoriamente maior que zero.
# Em seguida exiba na tela todos os números inteiros menores que 100 e que sejam divisíveis por D.

D = int(input('Digite D: '))
if D <= 0:
    print(f'O valor {D} é inválido')
else:
    i = 1
    while i < 100:
        if i % D == 0:
            print(i)
        i = i + 1
print('Fim do Programa')

# Digite D: 22
# 22
# 44
# 66
# 88
# Fim do Programa


# Neste exercício temos uma novidade: o valor de D deveria ser maior que zero.
# Usamos um comando if para fazer a verificação e se D <= zero, emitimos uma mensagem dizendo que é inválido.
# No else (que ocorrerá quando D for maior que zero) foi implementado o restante do código.
# Neste ponto foi implementado um laço de repetição baseado em um contador.
# O objeto i foi usado no controle do laço e cada vez que esse i era divisível por D seu valor foi exibido na tela.
# Podem existir comandos condicionais dentro de comandos de laço e vice-versa, sem limite de vezes em que isso ocorre.
