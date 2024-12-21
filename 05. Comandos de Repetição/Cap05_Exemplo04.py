# 5.3.3 CLÁUSULA else DO COMANDO while
# Em Python a forma completa do comando while inclui uma parte else,
# que parece muito estranha para os programadores que aprenderam a programar com outras linguagens.

# A forma geral do while é:
# while <condição>
#     <bloco de comandos 1 – que pode conter um break>
# else:
#     <bloco de comandos 2>

# Seu funcionamento ocorre assim: o laço é repetido normalmente enquanto a condição for verdadeira.
# Quando a condição se tornar falsa o laço termina e o código do else é executado.
# Se um comando break existir no laço e for executado, então o else não é executado.

X = 1
while X > 0:        # enquanto X for positivo faça as repetições
    X = int(input('Digite X: '))
    if X == 0:      # se X for zero interrompa o laço
        print('você digitou zero...')
        break
    print(X)
else:               # este else é executado quando X for negativo se X for zero não
    print('você digitou negativo')
print('Fim do Programa')

# Digite X: 2
# 2
# Digite X: 0
# você digitou zero...
# Fim do Programa

# Digite X: 5
# 5
# Digite X: -1
# -1
# você digitou negativo
# Fim do Programa
