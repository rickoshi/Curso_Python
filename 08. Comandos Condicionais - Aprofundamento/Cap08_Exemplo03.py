# COMANDO if DE ÚNICA LINHA
# Este tipo de comando existe em outras linguagens de programação como C e Java.
# Também é conhecido pelo termo "operador ternário".
# Seu objetivo é permitir uma escrita compacta a comandos condicionais do tipo if-else
# (no caso, sem a presença do elif) cujo código subordinado seja constituído por apenas uma instrução.
# Imagine que você precise escrever o seguinte condicional:

# if X >= Y:
#     print(X)
# else:
#     print(Y)

# Trata-se de um condicional muito simples e, no entanto, ele ocupa quatro linhas no seu código. Embora
# isso não represente um problema e o código seja legível e compreensível a forma alternativa usando o if de
# única linha é considerado por muitos programadores mais vantajosa. Sua forma é:

# print(X) if X >= Y else print(Y)

# Esta linha faz exatamente a mesma tarefa realizada nas quatro linhas anteriores. Veja o exemplo:
X = 10
Y = 9
print(f'X é maior = {X}') if X >= Y else print(f'Y é maior = {Y}')

# o inline-if acima é o mesmo que isto:
if X >= Y:
    print(f'X é maior = {X}')
else:
    print(f'Y é maior = {Y}')

# alterando o valor de Y obtemos a execução do else
Y = 11
print(f'X é maior = {X}') if X >= Y else print(f'Y é maior = {Y}')

# X é maior = 10
# X é maior = 10
# Y é maior = 11


# Perceba pelo exemplo que as duas formas de comando condicional – clássica e única linha –
# funcionam exatamente da mesma maneira. Desse modo, nos seus programas você pode adotar a maneira
# que considerar mais conveniente. Em termos de desempenho, ou seja, velocidade de execução do código,
# as duas formas são equivalentes e isso não será critério para escolha entre uma ou outra.

# Mas lembre-se que o if de única linha suporta apenas um comando nos blocos de instruções subordinadas.
# E se o seu código contém muitas linhas nesses blocos você terá que usar a forma clássica.
# Formalizando, o if de única linha tem a seguinte construção:

# <comando para verdadeiro> if <condição> else <comando para falso>

# Ele deve ser entendido assim: se a condição for verdadeira execute o comando para verdadeiro,
# senão execute o comando para falso.
