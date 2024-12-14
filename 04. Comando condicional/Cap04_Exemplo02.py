# CONCEITO GERAL DE UM COMANDO CONDICIONAL
# Ao utilizar o comando condicional será necessário formular uma condição cujo resultado será falso ou verdadeiro.
# Em função desse resultado o programa seguirá apenas um de dois possíveis caminhos distintos.
# A ideia básica é implementar um código que reflita esta frase:
# "se B for igual a zero, então apresente a mensagem 'Não é possível calcular a divisão',
# senão (ou seja, B é diferente de zero) calcule e apresente na tela A / B.

A = int(input('Digite A: '))
B = int(input('Digite B: '))
if B == 0:
    print('Não é possível calcular a divisão')
else:
    R = A / B
    print(R)

# primeira execução
# Digite A: 26
# Digite B: 0
# Não é possível calcular a divisão

# segunda execução
# Digite A: 26
# Digite B: 4
# 6.5

# INDENTAÇÃO
# No Python a indentação é obrigatória.
# Generalizando, todos os conjuntos de comandos subordinados devem estar indentados em relação ao seu comando
# Isso vale para if-else, while, for, try, def e qualquer outro elemento em que exista subordinação.
