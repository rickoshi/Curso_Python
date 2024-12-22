# Erros podem acontecer em um sistema computacional.
# Há erros de hardware, sistema operacional e há os erros dos programas de usuário final.
# O tratamento de exceções está relacionado com erros que podem acontecer em um programa.
# Esse termo, exceção, se refere às situações que necessitam de atenção e algum tratamento especial fora da
# lógica normal de processamento do programa.

# Essas situações estão sempre relacionadas aos dados que
# estão nos objetos e são decorrentes uma grande variedade de fatores, tais como:
# • Divisão por zero;
# • Erro de dados de entrada;
# • Indexadores de array fora dos limites corretos;
# • Erros da aplicação permitindo valores e formatos incorretos nos objetos; entre outros.
# A pequena lista acima não esgota todas as possibilidades de erros e falhas que podem ocorrer com os
# dados em um programa de computador. E quando qualquer desses fatores ocorre, o programa pode parar de
# funcionar podendo ocasionar vários tipos de contratempo e prejuízo. A elaboração de uma boa estratégia de
# tratamento de exceções permite a criação de programas robustos e confiáveis.

Dado = '13o5'
Valor = int(Dado)
print(Valor)

# Traceback (most recent call last):
#   File "Cap06_Exemplo01.py", line 19, in <module>
#     Valor = int(Dado)
#             ^^^^^^^^^
# ValueError: invalid literal for int() with base 10: '13o5'

# O objeto Dado foi carregado com o string '13o5' e em seguida houve a tentativa de convertê-lo para número inteiro.
# É uma situação que pode acontecer em que, por um engano de digitação do usuário,
# o programa recebeu uma letra 'o' no lugar do algarismo '0' e em virtude disso não é possível fazer a conversão.
# O erro gerado foi da classe ValueError e o programa parou de funcionar.
