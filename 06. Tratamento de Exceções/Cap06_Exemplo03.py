# TRATAMENTO DE EXCEÇÕES EM PYTHON – FORMA ESSENCIAL
# Para implementar o tratamento de exceções em Python utiliza-se o comando try-except.
# As linhas a seguir mostram a estrutura deste comando:

# try:
#     <bloco de código protegido>
# except:
#     <bloco de tratamento da exceção>

# O conceito envolvido neste comando é a proteção de um determinado bloco de código.
# A palavra-chave try dá início ao código protegido.
# Se algum erro ocorrer em qualquer linha deste bloco a execução é desviada para o bloco sob a cláusula except.

A = int(input('Digite A: '))
B = int(input('Digite B: '))
try:
    R = A / B
    print(f'Resultado = {R}')
except:
    print('Não é possível calcular a divisão')

# primeira execução
# Digite A: 20
# Digite B: 0
# Não é possível calcular a divisão

# segunda execução
# Digite A: 75
# Digite B: 4
# Resultado = 18.75


# Nesse código as leituras de A e B estão fora do try e não estão protegidas.
# O cálculo da divisão e o print() estão dentro do try e estão protegidos.
# O except define qual será o tratamento em caso de erro na parte protegida.

# Na primeira execução deste exemplo foi fornecido o valor 0 para B. Como isso gera o erro de divisão por
# zero a execução foi desviada para o except, dentro do qual é exibida a mensagem "Não é possível calcular a divisão".
# Na segunda execução o valor de B é diferente de zero, então as duas linhas do código protegido
# pelo try foram executadas e o resultado da divisão foi apresentado na tela.


# EXCEÇÕES NOMEADAS
# Toda exceção em Python é uma classe e tem um identificador. A título de exemplo, no início deste
# capítulo mostramos três classes de exceções: ZeroDivisionError, ValueError, IndexError

# Olhe para a primeira linha onde é feita a leitura de A.
# Considere que o usuário quisesse digitar 50, mas colocou a letra 'o' no lugar do zero.
# Isso vai gerar um ValueError e essa linha não está protegida.
# Vamos então fazer uma alteração e passar os comandos de leitura para dentro do bloco protegido pelo try.

try:
    A = int(input('Digite A: '))
    B = int(input('Digite B: '))
    R = A / B
    print(f'Resultado = {R}')
except:
    print('Não é possível calcular a divisão')

# primeira execução
# Digite A: 20
# Digite B: 0
# Não é possível calcular a divisão

# segunda execução
# Digite A: 5o
# Não é possível calcular a divisão


# A questão da proteção está resolvida, mas agora temos outro problema.
# Qualquer erro que ocorra vai desviar para o except e dar a mesma mensagem " Não é possível calcular a divisão",
# independente de qual erro realmente ocorreu: se foi na leitura de um dado (ValueError) ou se foi divisão por zero
# (ZeroDivisionError). Para programas profissionais isso não é nada adequado.
