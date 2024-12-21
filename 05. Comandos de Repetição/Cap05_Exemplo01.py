# Muitas vezes um determinado bloco de código precisa ser repetido várias vezes.
# A esta situação de execução de repetições em um programa damos o nome de "laço de repetição" ou "loop de repetição".
# Na linguagem Python existem dois comandos que realizam repetições:
# • Comando while: este é o comando de repetição de uso geral;
# • Comando for: este comando é para uso especializado;

# 5.1 O COMANDO while
# 5.1.1 COMO IMPLEMENTAR UM LAÇO DE REPETIÇÃO EM PYTHON
# O comando while em Python tem a construção básica abaixo que pode ser interpretada como:
# "enquanto a condição for verdadeira execute o conjunto de comandos".

# while <condição>:
#     <conjunto de comandos>

# A condição segue as mesmas regras utilizadas nas condições quando tratamos do comando if–else.
# Os comandos subordinados ao while, podem ser quaisquer comandos válidos em Python, em qualquer quantidade e extensão.
# A indentação é importante pois define a relação de subordinação entre o comando e seu bloco de código subordinado.

print("Início do Programa")
cont = 1                # linha 1
while cont <= 10:       # linha 2
    print(cont)         # linha 3
    cont = cont + 1     # linha 4
print("Fim do Programa")

# Início do Programa
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Fim do Programa

# 5.1.2 FLUXO DE EXECUÇÃO DE LAÇOS DE REPETIÇÃO while
# O primeiro ponto é saber que o teste da condição é feito no início do laço.
# A avaliação da condição é feita antes de se executar o conjunto de comandos subordinado.
# Este fato tem uma implicação conceitual importante porque nos casos em que a condição for previamente falsa
# o conjunto subordinado não será executado nenhuma vez.

# Qualquer laço para ser implementado requer quatro elementos:
# • Inicialização: situação inicial do controle do laço;
# • Condição de continuidade do laço;
# • Iteração: ação sobre o controle do laço, a cada repetição; e
# • Corpo: bloco de código subordinado.

# Os três primeiros dizem respeito à estrutura e controle do laço.
# A inicialização constitui-se do código necessário para determinar a situação inicial do laço.
# A condição de continuidade é uma expressão lógica, simples ou composta,
# cujo resultado é avaliado em falso ou verdadeiro a cada repetição e que
# determinará se o laço termina ou prossegue, respectivamente.
# A iteração é o comando (um ou mais de um) que modifica os objetos envolvidos na condição de continuidade,
# a cada execução do laço.
