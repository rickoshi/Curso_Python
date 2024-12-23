# Enunciado: Escreva um programa que permaneça em laço lendo números inteiros. O laço termina quando for
# digitado 0 (zero). Cada valor diferente de zero digitado deve ser colocado em uma lista. Ao final exiba
# a lista na tela e a quantidade de elementos que ela contém.

LstValores = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    LstValores.append(valor)
    valor = int(input('Digite um inteiro: '))
print('\nResultado')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos')
print('Fim do Programa')

# Digite um inteiro: 138
# Digite um inteiro: -79
# Digite um inteiro: -14
# Digite um inteiro: 63
# Digite um inteiro: -49
# Digite um inteiro: 41
# Digite um inteiro: 0
#
# Resultado
# [138, -79, -14, 63, -49, 41]
# A lista contém 6 elementos
# Fim do Programa


# Perceba que nesta solução foi usado o comando while ao invés do for. O motivo é o fato de que não
# sabemos quantas vezes o laço irá se repetir. Como o enunciado impõe que o laço só termina quando o dado
# de entrada for 0 (zero), a permanência das repetições depende daquilo que o usuário digita. Este é um
# exemplo de situação em que não é possível usar o comando for.

# Outra restrição do enunciado é: "cada valor diferente de zero deve ser colocado em uma lista", ou seja,
# o zero não pode entrar na lista. Para lidar com esta restrição foi usada a técnica de "aquisição do dado na
# saída do laço". Isso é um aspecto de lógica que se aplica a qualquer linguagem. Para implementar essa
# técnica fazemos a leitura do primeiro dado antes do laço começar; dentro do laço o primeiro dado é
# processado e a última tarefa dentro do laço é ler o próximo dado – se esse dado lido for zero o laço termina,
# mas se não for o laço continua e já podemos processar o novo dado. A alternativa a isso seria o código abaixo:

# valor = 1
# while valor != 0:
#    valor = int(input('Digite um inteiro: '))
#    if valor != 0:
#        LstValores.append(valor)

# Nesta alternativa temos que garantir que o laço inicie, para isso fizemos valor = 1 e dentro do laço
# temos que acrescentar um if para garantir que o zero não entre na lista.
