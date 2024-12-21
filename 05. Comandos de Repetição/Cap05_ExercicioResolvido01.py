# Enunciado: Escreva um programa que permaneça em laço enquanto um valor X lido for diferente de zero.
# Para cada valor de X apresente na tela se é par ou ímpar.

X = 1
while X != 0:
    X = int(input('Digite X: '))
    if X % 2 == 0:
        print(f'{X} é par')
    else:
        print(f'{X} é ímpar')
print("Fim do Programa")

# Digite X: 34
# 34 é par
# Digite X: 21
# 21 é ímpar
# Digite X: 0
# 0 é par
# Fim do Programa


# Nesta solução o controle do laço é realizado de forma diferente.
# Desta vez não temos um contador, ou seja, a natureza do controle do laço é de outro tipo.
# Para garantir que o laço seja iniciado, o objeto X deve ser criado contendo qualquer valor diferente de 0.
# A linha 1 é a linha de inicialização. A Iteração é implementada na linha 3 que altera o valor do objeto X.
# O novo X lido logo no início do laço também é usado no corpo do mesmo, que é constituído pelas linhas 4 a 7.
# O resto da divisão de X por 2 é calculado e comparado com zero.
# Se o resultado dessa comparação for verdadeiro, então o número é par, caso contrário é ímpar.
# Quando zero for digitado, o programa dirá que zero é par e terminará.
