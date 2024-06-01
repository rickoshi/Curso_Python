# Importar por módulos
# from (biblioteca) import (módulo)
# from math import *
from math import sqrt
X = 49
R = sqrt(X)
print(R)            # 7.0

# Import a biblioteca completa e chama-lá junto com a função
import math
T = math.sqrt(X)
print(T)            # 7.0
print(math.pi)      # 3.141592653589793

T = math.sin(math.pi / 2)
print(T)            # 1.0

U = math.cos(math.pi / 2)
print(U)            # 6.123233995736766e-17
print(round(U))     # 0
print(round(U, 3))  # 0.0

a = 18.714869999
b = round(a, 5)
print(a)            # 18.714869999
print(b)            # 18.71487

# Biblioteca math - Funções com valores numéricos inteiros e reais
# Biblioteca cmath - Funções com valores numéricos complexos
# Consultar na documentação Python todas as funções existentes
