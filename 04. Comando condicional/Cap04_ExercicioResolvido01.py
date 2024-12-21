# Enunciado: Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
# Lembrando que para saber a paridade de um inteiro é preciso calcular o resto da sua divisão por 2.
# Se o resto for 0 o número é par, se o resto for 1 o número é ímpar.

X = int(input('Digite um inteiro: '))
Resto = X % 2                               # Calcula o resto da divisão de X por 2
if Resto == 0:                              # Verifica se o resto é 0
    print(f'O número {X} é par')
else:                                       # Se a condição resultou False desvia para este else
    print(f'O número {X} é ímpar')
print('Fim do Programa')

# # primeira execução
# Digite um inteiro: 82
# O número 82 é par
# Fim do Programa

# segunda execução
# Digite um inteiro: 53
# O número 53 é ímpar
# Fim do Programa
