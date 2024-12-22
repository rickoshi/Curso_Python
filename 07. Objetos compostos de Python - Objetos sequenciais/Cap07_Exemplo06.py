# O Ptyhon não permite indexação fora dos limites. Se houver a tentativa de usar um índice de elemento
# (positivos ou negativos) que não existe uma exceção IndexError será gerada.

A = [10, 12, 14, 16]
print(A[9])

# Traceback (most recent call last):
#   File "Cap07_Exemplo06.py", line 5, in <module>
#     print(A[9])
#           ~^^^
# IndexError: list index out of range
