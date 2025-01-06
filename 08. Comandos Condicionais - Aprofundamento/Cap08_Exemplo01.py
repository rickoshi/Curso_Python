# COMANDO MATCH-CASE
# O comando match-case foi introduzido na linguagem Python a partir da versão 3.10.
# Esse comando se assemelha a um comando switch em C ou Java.
# Este comando toma uma expressão e compara seu conteúdo com valores sucessivos dispostos em cláusulas case,
# buscando verificar se há correspondência, sendo que tais cláusulas são mutuamente exclusivas.
# Desse modo, ele permite implementar algoritmos onde múltiplos testes precisam ser realizados.
# A estrutura do comando é esta:

# match <expressão>:
#     case <valor1>:
#         <bloco de comandos 1>
#     case <valor2>:
#         <bloco de comandos 2>
#     ...
#     case _:
#         <bloco de comandos final>

# A expressão pode ser um objeto, uma expressão aritmética ou o retorno de uma função.
# Qualquer dessas opções conterá um valor que será comparado com valor1, se houver correspondência o bloco de
# comandos 1 será executado e todos os demais blocos serão ignorados; caso não haja correspondência com
# o valor1, então será testada a correspondência com o valor2 executando o bloco de comandos 2 e assim sucessivamente.
# Ao final, não havendo correspondência com nenhum dos valores listados, e havendo
# a cláusula case _ (case underline) então o bloco subordinado a ela será executado. A ordem das cláusulas
# case não importam, não sendo necessário que estejam ordenadas, contanto que a última delas seja a que
# contém o underline: case _.

n = -1
while n != 0:
    n = int(input('Digite um inteiro: '))
    match n:
        case 1:
            print(' você digitou um')
        case 2:
            print(' você digitou dois')
        case 3:
            print(' você digitou três')
        case _:
            print(' você digitou outra coisa')
print('Fim do Programa')

# Digite um inteiro: 1
#  você digitou um
# Digite um inteiro: 2
#  você digitou dois
# Digite um inteiro: 3
#  você digitou três
# Digite um inteiro: 4
#  você digitou outra coisa
# Digite um inteiro: 0
#  você digitou outra coisa
# Fim do Programa


# Neste exemplo o programa fica em laço enquanto o objeto inteiro n for diferente de 0. Dentro do laço,
# cada valor lido em n será processado pelo comando match realizando as verificações de correspondências
# com cada uma das cláusulas case e processando o código adequado.
