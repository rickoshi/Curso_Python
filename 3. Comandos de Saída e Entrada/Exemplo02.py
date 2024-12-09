# Quando os conteúdos de dois objetos são exibidos simultaneamente,
# Os valores são exibidos na mesma linha separados por um espaço em branco.
# O espaço em branco está pré-configurado no parâmetro sep.
# É possível alterar esse caractere separador especificando-se um texto alternativo atribuído à sep.

A = 12
B = 19
print(A, B)                 # 12 19
print(A, B, sep='-')        # 12-19
print(A, B, sep=' - ')      # 12 - 19
print(A, B, sep='<-->')     # 12<-->19
print(A, B, sep=', ')       # 12, 19

print('um\ndois\ntrês')
# um
# dois
# três

print('um\tdois\ttrês')     # um	dois	três

# Modificando o parâmetro end, conseguimos modificar o caractere no final para a saída
X = 12
Y = 26
print(X)                # 12
print(Y)                # 26
print(X, end='...')     # 12...
print(Y)                # 26
# 12...26
