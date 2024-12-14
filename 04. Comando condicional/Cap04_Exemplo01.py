# CONCEITO GERAL DE UM COMANDO CONDICIONAL
# É muito frequente a necessidade de tomada de decisão em um programa de computador,
# assim como acontece em situações comuns, por exemplo:
# "se estiver frio coloque use o casaco, senão tire o casaco"

# Em programação essas decisões são baseadas em valores contidos em objetos.
# Por exemplo, considere uma situação que envolva dois objetos da classe int A e B previamente carregados.
# Caso seja necessário calcular a divisão de A por B e o conteúdo do objeto B for zero, ocorrerá um erro,
# O motivo do erro é que divisões por zero não são permitidas.

A = 10
B = 0
R = A / B       # ZeroDivisionError: division by zero
print(R)        # Comando não executado

# Situações de erro assim são indesejáveis e é preciso tomar o cuidado de se evitá-las.
# Uma das formas (não a única) de se conseguir isso é usar o Comando Condicional: if-else.
