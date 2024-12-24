# Saída formatada
# A saída formatada é útil para criar exibições de fácil leitura, pois permite controlar detalhes da exibição dos dados.
# A função print() não é a responsável pela formatação. O papel dela se limita a direcionar os textos ao dispositivo.
# A formatação é realizada pelos métodos disponíveis na classe str.

X = 26
Y = 58
s = "Valores: X = {0} e Y = {1}".format(X, Y)
print(s)        # Valores: X = 26 e Y = 58


# FORMATAÇÃO USANDO O MÉTODO .format()
# O primeiro passo é definir como se quer o texto final, tomando o cuidado de utilizar os marcadores {0}, {1}, {2} etc.
# nos pontos onde se deseja que apareça o conteúdo dos objetos envolvidos.
# O texto deve ser seguido do método .format(), que conterá como argumentos os objetos que fornecerão os valores.
# A substituição dos marcadores pelos argumentos é feita seguindo-se o índice numérico.

print("Valor de X = {0} e valor de Y = {1}".format(X, Y))   # Valor de X = 26 e valor de Y = 58
print("Valor de X = {1} e valor de Y = {0}".format(X, Y))   # Valor de X = 58 e valor de Y = 26

# Opcionalmente é possível omitir o número dentro das chaves dos marcadores, utilizando apenas {}.
# Neste caso, a associação entre marcador e objeto será feita pela ordem de ocorrência.

print("Valor de X = {} e valor de Y = {}".format(X, Y))     # Valor de X = 26 e valor de Y = 58


# Os marcadores podem receber qualificadores de formatação. Isso é feito através do uso do caractere ":".
# São comuns três qualificadores de formatação para os seguintes aspectos:
# - Tipo de apresentação: inteiro decimal, binário ou hexadecimal; real; caractere;
# - Tamanho da apresentação: quantidade de caracteres a serem usados e opcionalmente quantidade de casas decimais;
# - Alinhamento da apresentação: especifica se um dado será alinhado à esquerda, à direita ou centralizado;

A = 9
X = 4.86

print("Dado = {:d}".format(A))      # Dado = 9          d – número inteiro, em base 10
print("Dado = {:5d}".format(A))     # Dado =     9      5d – número inteiro, mínimo 5 caracteres alinhado à direita
print("Dado = {:f}".format(X))      # Dado = 4.860000   f – número real, exibindo o padrão de 6 casas após a vírgula
print("Dado = {:7.3f}".format(X))   # Dado =   4.860    f – número real, mínimo 7 caracteres, 3 casas após a vírgula
print("Dado = {:.2f}".format(X))    # Dado = 4.86       f – número real, 2 casas após a vírgula.
print("..{:>7d}..".format(A))       # ..      9..       7d – número inteiro, mínimo 7 caracteres alinhado à direita
print("..{:<7d}..".format(A))       # ..9      ..       7d – número inteiro, mínimo 7 caracteres alinhado à esquerda
print("..{:^7d}..".format(A))       # ..   9   ..       7d – número  inteiro, mínimo 7 caracteres centralizado
