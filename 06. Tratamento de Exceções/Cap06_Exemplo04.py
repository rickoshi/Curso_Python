# Para promover um tratamento adequado a cada situação pode-se identificar a classe da exceção na cláusula except.
#
# Foram usados dois excepts nomeados e um genérico.
# Quando ocorre um erro o interpretador Python primeiro procura a existência de um except nomeado
# e se encontrar desvia a execução para ele; caso contrário ele executa o except genérico (não nomeado).
# Só pode haver um except genérico.

try:
    A = int(input('Digite A: '))
    B = int(input('Digite B: '))
    R = A / B
    print(f'Resultado = {R}')
except ZeroDivisionError:           # except nomeado
    print('B não pode ser zero')
except ValueError:                  # except nomeado
    print('Digite números inteiros para A e B')
except:                             # except genérico (não-nomeado)
    print('Não é possível calcular a divisão. Erro desconhecido')

# primeira execução
# Digite A: 20
# Digite B: 0
# B não pode ser zero

# segunda execução
# Digite A: texto
# Digite números inteiros para A e B

# terceira execução
# Digite A: 18
# Digite B: 4
# Resultado = 4.5


# TRATAMENTO DE EXCEÇÕES EM PYTHON – FORMA COMPLETA
# O comando try tem outros dois blocos ainda não mencionados e serão vistos agora.
# As linhas abaixo mostram sua estrutura completa

# try:
#     <bloco 1>
# except:
#     <bloco 2>
# else:
#     <bloco 3>
# finally:
#     <bloco 4>

# O comando try, além dos vários blocos except, contém outras duas cláusulas opcionais: else e finally.
# Essas cláusulas devem ser colocadas nessa ordem.

# Quando o bloco 1 é executado ele está protegido. Supondo que nenhum erro ocorra, imediatamente
# após seu término é feita a execução do bloco 3 que está no else. Se alguma exceção ocorrer o código de
# tratamento no except é executado e o código do else não é executado.

# A outra parte opcional finally sempre é executada, ocorra erro ou não. Se uma cláusula finally
# estiver presente, ela será executada como a última tarefa antes da conclusão da instrução try. Se ambos,
# else e finally, estiverem presentes o else será executado antes do finally.

# O objetivo da cláusula finally é permitir a implementação de ações de finalização e limpeza, que
# eventualmente sejam necessárias independentemente da ocorrência de exceções, por exemplo: eliminação
# de arquivos temporários; fechamento de conexão com o banco de dados; ou a liberação de recursos de rede.
