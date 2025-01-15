# O exemplo a seguir reproduz o exemplo 9.6 (operações com conjunto), porém com o uso de frozenset

A = frozenset('ANTONIO CARLOS')
print(A)                # frozenset({' ', 'S', 'I', 'L', 'A', 'T', 'R', 'N', 'O', 'C'})
B = frozenset('JOSÉ CARLOS')
print(B)                # frozenset({'É', ' ', 'S', 'L', 'A', 'J', 'R', 'O', 'C'})
print(A - B)            # frozenset({'T', 'N', 'I'})
print(B - A)            # frozenset({'É', 'J'})
print(A | B)            # frozenset({'S', 'L', 'J', 'T', 'R', 'C', 'É', ' ', 'I', 'A', 'N', 'O'})
print(A & B)            # frozenset({' ', 'S', 'L', 'A', 'R', 'O', 'C'})
print(A ^ B)            # frozenset({'É', 'I', 'J', 'T', 'N'})
print('X' in A)         # False
print('T' in A)         # True
print('X' not in A)     # True
print('T' not in A)     # False
