# A FUNÇÃO input()
# É preciso que permitir que dados sejam digitados e inseridos em objetos do programa.
# Em Python 3 quem realiza essa tarefa é a função input().
# Para usá-lo basta atribuir seu retorno a algum identificador.
# Opcionalmente pode-se passar um parâmetro que será usado como uma mensagem que indique o que deve ser digitado.

# A primeira leitura carrega o objeto A sem mostrar qualquer mensagem na tela.
A = input()
# Digitei isto
print(A)        # Digitei isto

# Na segunda leitura é apresentada a mensagem "Digite algo: ",
# indicando o que deve ser feito e no retorno dessa função o objeto B é carregado.
B = input('Digite algo: ')
# Digite algo: Digite isto
print(B)        # Digitei isto

# Quando a função input() é executada o computador aguarda a entrada seguida de "Enter",
# tudo o que foi digitado é carregado no objeto que recebe o retorno da função.
# O usuário pode digitar e a leitura sempre resulta em uma cadeia de caracteres (string) carregada no objeto de destino.
