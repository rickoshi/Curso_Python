# OPERADOR in
# O operador in permite ao programador verificar se um valor está presente em uma lista.
# Alternativamente pode-se usá-lo na forma not in para verificar se um valor não está na lista.
# Este é um operador de uso geral em Python. Portanto, seu uso não é restrito às listas, podendo ser
# usado com a maioria das classes de objetos compostos.

L = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
print(25 in L)          # True      |   25 está em L, então in retornou True
print(99 in L)          # False     |   99 não está em L, então in retornou False
print(25 not in L)      # False     |   25 está em L, então not in retornou False
print(99 not in L)      # True      |   99 não está em L, então not in retornou True
