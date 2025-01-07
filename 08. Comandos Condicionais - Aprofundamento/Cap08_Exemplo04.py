# OBRIGATORIEDADE DO else
# Essa forma deve sempre ser usada completa, ou seja, a parte do else é obrigatória não podendo ser omitida.
# Mas há situações nas quais precisamos implantar um código que não tenha o else. Imagine uma
# situação em que tenhamos uma lista de códigos de produto e desejamos filtrar os códigos dentro de uma
# certa faixa de valores, por exemplo entre 120 e 200. Códigos fora dessa faixa não nos interessa. Para
# implementar algo assim poderíamos escrever o código abaixo no qual o else é desnecessário.

# laço while ou for ...
#     if codigo >= 120 and codigo <= 200:
#         Lista.append(codigo)

# Ainda assim é possível fazê-lo com um if de única linha, conforme mostrado no exemplo a seguir:

Codigos = [103, 117, 121, 135, 161, 189, 200, 204, 216]
Lista = []
print('Alternativa com if clássico')
for codigo in Codigos:
    if 120 <= codigo <= 200:
        Lista.append(codigo)
print(f' códigos filtrados -> {Lista}')

print('\nAlternativa com if de única linha')
Lista = []
for codigo in Codigos:
    Lista.append(codigo) if 120 <= codigo <= 200 else 0
print(f' códigos filtrados -> {Lista}')

# Alternativa com if clássico
#  códigos filtrados -> [121, 135, 161, 189, 200]
#
# Alternativa com if de única linha
#  códigos filtrados -> [121, 135, 161, 189, 200]


# Perceba que bastou colocar else 0 no if de única linha e as duas alternativas produziram o mesmo resultado.
# Com isso você já sabe como usar essa forma de comando condicional mesmo que não necessite da parte else.
