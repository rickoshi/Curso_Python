# A leitura sempre resulta em uma cadeia de caracteres (string) carregada no objeto de destino.
# Se forem digitados apenas algarismos, ainda assim a leitura resulta em uma cadeia de caracteres.

# O objeto N aparentemente recebe um número inteiro e F aparentemente recebe um número real.
# Porém, ao utilizar o comando type, verifica-se que ambos são do tipo da classe str.

N = input("Digite um inteiro: ")
# Digite um inteiro: 37
print(N)            # 37
print(type(N))      # <class 'str'>

F = input("Digite um real: ")
# Digite um real: 31.47
print(F)            # 31.47
print(type(F))      # <class 'str'>
