# CONDIÇÕES SIMPLES
# O pilar do comando condicional é a condição que será avaliada e cujo resultado pode ser falso ou verdadeiro.
# Existem condições simples e compostas.
# A condição B == 0 é uma condição simples, pois ela tem a seguinte construção:
# <expressão 1> <operador> <expressão 2>

# Onde as expressões 1 e 2 podem ser uma dessas possibilidades:
# • um literal (geralmente número ou texto)
# • um objeto
# • uma fórmula (expressão aritmética)
# • uma chamada de função

# O operador é um de seis operadores relacionais.
# No caso dos operadores que contém dois caracteres, não é permitido haver espaço em branco entre eles.

# Operador      Como se lê          Interpretação
#    ==         Igual a             X == Y : retorna True se X e Y são iguais, caso contrário retorna False
#    !=         Diferente de        X != Y : retorna True se X e Y são diferentes, caso contrário retorna False
#     <         Menor que           X < Y : retorna True se X for menor que Y, caso contrário retorna False
#    <=         Menor ou igual a    X <= Y : retorna True se X for menor ou igual a Y, caso contrário retorna False
#     >         Maior que           X < Y : retorna True se X for maior que Y, caso contrário retorna False
#    >=         Maior ou igual a    X < Y : retorna True se X for maior ou igual aY, caso contrário retorna False


A = 10
B = 50

# Comparação entre objeto e literal
print(A > 0)                # True

# Comparação entre objeto e literal
print(B <= 0)               # False

# Comparação entre dois objetos
print(A >= B)               # False

# Comparação entre fórmula e objeto
print(5 * A == B)           # True

# Comparação entre objeto e função
print(A >= pow(B, 0.5))     # True
