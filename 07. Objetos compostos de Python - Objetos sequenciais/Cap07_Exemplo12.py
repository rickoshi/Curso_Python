# O COMANDO for
# Já foi mencionado que o comando for é um comando de repetição. Portanto, serve para a criação de laços de repetição,
# mas ele é bem diferente do comando while. Podemos dizer que o while é um comando de repetição de uso geral,
# enquanto o for tem um uso bem específico.
# O comando for é usado para iterar sobre os elementos de qualquer objeto estruturado de Python, tais como:
# listas, strings, tuplas, dicionários, conjuntos, etc.

# Iterar e Iteração
# Iterar é percorrer os elementos de uma sequência,
# na ordem em que eles estão dentro dela e
# realizar um processamento com cada um.
# Iteração é o processo de iterar.

# Neste exemplo uma lista com 4 números inteiros é criada e em seguida o comando for é usado para iterar sobre ela.
# Para tornar a iteração possível o objeto valor tem papel preponderante.
# Ele recebe cada elemento contido na lista L, um por vez, ou seja, um objeto de L a cada repetição.
# E dentro do laço valor pode ser usado normalmente para qualquer fim que o programador necessite.

L = [21, 45, 17, 28]
pos = 0
for valor in L:
    print(f'A posição {pos} contém {valor}')
    pos += 1
print('Fim do Programa')

# A posição 0 contém 21
# A posição 1 contém 45
# A posição 2 contém 17
# A posição 3 contém 28
# Fim do Programa


# A descrição formal do funcionamento do comando for é a seguinte:

# for objctrl in objseq:
#     bloco1
# else:
#     bloco2

# a) O objeto objseq é avaliado para verificar se é um objeto válido para o comando for.
# Se não for válido um erro é gerado e o processo termina; se for válido avança para o próximo passo;
# b) O objeto objctrl recebe o primeiro elemento de objseq e o bloco1 é executado uma vez;
# c) Ao término da execução do bloco1 o objctrl recebe o próximo elemento de objseq e o bloco1 é executado novamente.
# Isto se repete para cada item presente em objseq.
# Caso o laço de repetição termine normalmente o bloco2 dentro o else é executado.

# Os comandos continue e break, vistos quando falamos do comando while, também se aplicam ao comando for.
# • O comando continue executado no bloco1 interrompe a atual repetição e continua com o próximo item;
# • O comando break executado no bloco1 termina o laço de repetição. Se isto ocorrer o bloco2
# dentro da cláusula else não será executado.
