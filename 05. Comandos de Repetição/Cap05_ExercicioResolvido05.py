# Enunciado: Escreva um programa que permaneça em laço enquanto um valor inteiro lido for diferente de zero.
# Totalize e conte os valores digitados, exceto o zero, e apresente esses valores na tela. Totalizar é somar os valores.

soma = qtde = 0
A = 1
while A != 0:
    A = int(input("Digite X: "))
    if A != 0:
        soma = soma + A
        qtde = qtde + 1
print(f'Soma dos valores = {soma}')
print(f'Quantidade = {qtde}')
print('Fim do Programa')

# Digite X: 16
# Digite X: 40
# Digite X: 21
# Digite X: 6
# Digite X: 0
# Soma dos valores = 83
# Quantidade = 4
# Fim do Programa


# Neste programa o controle do laço se faz através do objeto A que é lido a cada repetição.
# Quando for digitado o valor 0 para A o laço irá terminar e é preciso não somar 1 no objeto qtde quando isso ocorrer.
# Por esse motivo foi usado o comando condicional if A != 0 dentro do laço.
