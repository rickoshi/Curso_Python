# USO CONJUNTO DO INPUT COM FUNÇÕES DE CONVERSÃO
# É muito comum que nos programas seja necessário ler números inteiros e reais.
# Como a função input() sempre lê strings, será necessário executar uma conversão depois da leitura, ou seja,
# a leitura de valores numéricos, inteiros, reais ou complexos, é uma operação de duas etapas.

A = input('Digite A: ')         # lê o teclado e carrega A com um string
A = int(A)                      # converte A para inteiro e coloca esse inteiro em A

# A segunda linha merece atenção. Note que o objeto A está presente no lado esquerdo e direito do comando.
# Em situações assim sempre olhe primeiro para o lado direito e entenda o que ele faz:
# neste caso string do objeto A está sendo convertido para número inteiro com o uso da função int().
# Depois, olhe para o lado esquerdo e verifique que o objeto A está recebendo o resultado da conversão.
# Como objetos da classe str são imutáveis o objeto anterior será excluído e um novo objeto A será criado,
# desta vez baseado na classe int e receberá o valor convertido.

# Entendido o processo, podemos escrever o código do seguinte jeito:
A = int(input('Digite A: '))    # lê o teclado, converte para int e carrega A com ele

# Agora as duas operações ainda estão presentes, porém escritas em uma única linha e tornando o código mais compacto.
# Esta forma é a mais usada nos programas Python.
