x = 50
y = 12 + 38
z = 100 - 50

print(x, y, z)  # 50 50 50
print(id(x))    # 140714838925272
print(id(y))    # 140714838925272
print(id(z))    # 140714838925272

# Objetos Imutáveis
# Se o valor do objeto é alterado, o id também é alterado
z = 90

print(x, y, z)  # 50 50 90
print(id(x))    # 140714838925272
print(id(y))    # 140714838925272
print(id(z))    # 140714838926552
# o objeto 'z' é imutável, pois seu id mudou
