# 5.3.1 COMANDO CONTINUE
# O comando continue altera o fluxo normal de execução de um laço de repetição.
# Ele é usado para interromper uma repetição que esteja em curso dentro de um laço e avançar para a próxima repetição.
# Este exemplo foi criado para exibir valores de 1 a 5 na tela, com exceção do 4.
# O objeto i é usado no controle do laço e também é exibido na tela.
# Porém, quando ele assume o valor 4, o if dentro do laço resulta verdadeiro
# e o comando continue é executado interrompendo a atual execução e seguindo para a próxima.
# Como o print() está após esse código ele acaba sendo pulado e o valor 4 não é exibido na tela.

i = 0
while i < 5:
    i = i + 1
    if i == 4:
        continue        # Quando o continue é executado, é retornado ao cabeçalho do comando de repetição
    print(i)

# 1
# 2
# 3
# 5


# É preciso ter cuidado, pois é comum que o programador inexperiente cometa erros ao usá-lo de forma inadequada:
i = 0
while i < 5:
    if i == 4:
        continue
    i = i + 1        # A mudança de posição desta linha é a única alteração.
    print(i)

# Uma simples alteração de posição na linha i = i + 1 e este código fica totalmente errado.
# Quando o valor de i chegar a 4 será executado o continue sem passar pela linha do incremento de i.
# Isso implica que o valor de i será 4 para sempre e esse laço executará indefinidamente.
# É o que se chama de laço infinito, um erro severo, pois seu programa parecerá congelado,
# não exibindo nada na tela e nem respondendo ao usuário.
