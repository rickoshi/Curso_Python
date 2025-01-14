# Enunciado: Escreva um programa que leia um inteiro Qtde e crie um conjunto com elementos numéricos inteiros
# aleatórios dentro do intervalo fechado [1, 50]. Mostre o conjunto gerado na tela.
# Lembre-se que os conjuntos não podem ter elementos repetidos, então a geração de números
# aleatórios pode representar um problema. Como resolver isso?

# Cuidado: Este programa tem potencial para entrar em laço infinito caso o valor fornecido para Qtde seja maior
# que 50. Faça o teste e depois responda a pergunta: por que isso ocorre?

from random import randint
Qtde = int(input('Digite a quantidade: '))
while Qtde > 50:
    print('Valor muito alto')
    Qtde = int(input('Digite a quantidade (max 50) '))
conjunto = set()
while len(conjunto) < Qtde:
    conjunto.add(randint(1, 50))
print(conjunto)
print('Fim do Programa')

# primeira execução
# Digite a quantidade: 12
# {1, 34, 4, 40, 8, 11, 46, 17, 19, 22, 24, 31}
# Fim do Programa

# segunda execução
# Digite a quantidade: 60 # qualquer qtde > 50 faz o programa ficar em laço infinito


# A segunda execução do exercício resolvido foi inserida para mostrar como esse algoritmo entrará
# em laço infinito quando a quantidade fornecida for maior que 50. Assim respondendo à pergunta proposta no
# enunciado: isso ocorre porque a geração de números aleatórios está limitada a 50 valores (de 1 a 50). Como
# o conjunto não pode conter valores repetidos, então não há possibilidade matemática desse conjunto ser criado.
# O próximo passo é elaborar alguma forma de controle para este programa, para evitar que a situação
# de laço infinito ocorra. Uma possibilidade é validar o valor fornecido para Qtde e não aceita-lo caso o valor
# digitado seja maior que 50.
