# 5.3.2 COMANDO BREAK
# O comando break também altera o fluxo de execução de um laço de repetição.
# Quando executado o break o laço é encerrado imediatamente.
# Neste exemplo fizemos um laço infinito por definição ao escrever while True.
# Observe que está sendo usado o comando break, o que significa que esse laço não é verdadeiramente infinito.
# Quando o usuário digitar 0 (zero) o if dentro do laço resultará verdadeiro e o break interomperá o laço.

X = 1
while True:
    X = int(input('Digite X: '))
    if X == 0:
        print(' você digitou zero...')
        break           # Quando o break é executado o laço termina imediatamente
    print(X)
print('Fim do Programa')

# Digite X: 8
# 8
# Digite X: -4
# -4
# Digite X: 1
# 1
# Digite X: 0
#  você digitou zero...
# Fim do Programa
