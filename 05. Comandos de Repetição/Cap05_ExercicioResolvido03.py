# Enunciado: Escreva um programa que mostre na tela os 10 primeiros termos de uma progressão aritmética (PA)
# com primeiro termo P e razão R. Os dois números P e R são inteiros e devem ser lidos do teclado.

P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
cont = 0
while cont < 10:
    print(P)
    P = P + R
    cont = cont + 1
print('Fim do Programa')

# Digite o primeiro termo: 4
# Digite a razão: 5
# 4
# 9
# 14
# 19
# 24
# 29
# 34
# 39
# 44
# 49
# Fim do Programa


# Nas duas primeiras linhas é feita a leitura dos dados. Em seguida é implementado o laço de repetição
# com o objeto cont inicializado em 0; a condição de continuidade cont < 10;
# e o incremento cont = cont + 1 alterando o objeto de controle do laço.

# A cada repetição um termo da PA é exibido e o próximo é calculado.
# Propositalmente, neste exercício o objeto cont foi inicializado com 0 e a condição foi escrita como cont < 10.
# Compare-a com o exemplo 5.1 onde o objeto cont foi iniciado com 1 e a condição escrita como cont <= 10.
# Estas são duas formas diferentes de implementar um laço que executa o mesmo número de vezes.
# Em situações como essa cabe ao programador escolher a alternativa que considera mais interessante para o programa.
