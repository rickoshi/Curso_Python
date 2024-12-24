A = 10
print(A)        # 10

A = A + 1
print(A)        # 11

A += 1          # Equivalente a fazer A = A + 1
print(A)        # 12

A = 10
P = 4
A += P          # A = A + P
print(A)        # 14

A -= P
print(A)        # 10

A *= P
print(A)        # 40

A /= P
print(A)        # 10.0
print(type(A))  # <class 'float'>

A = 40
A //= P
print(A)        # 10
print(type(A))  # <class 'int'>
