# FUNÇÕES DE CONVERSÃO DE OBJETOS DE CLASSES SIMPLES
# Estas funções permitem realizar a conversão entre tipos de dados simples

# Função                # Descrição
# int(objeto, base)     Converte o objeto para um número inteiro, se for possível. Se base não for fornecida
#                       será usada a base 10. As bases permitidas variam de 2 a 36.
# float(objeto)         Converte o objeto para um número real, se for possível.
# complex(objeto)       Converte o objeto para um número complexo, se for possível.
# bool(objeto)          Converte o objeto para um booleano, se for possível.
# str(objeto)           Converte o objeto para string

x = '19'
print(type(x))      # <class 'str'>

a = int(x)
print(type(a))      # <class 'int'>

x = '3.75'
print(type(x))      # <class 'str'>

r = float(x)
print(type(r))      # <class 'float'>

b = a + r           # soma um int (a==int(x)) com um float (r==float(x)), produzindo um float em b
print(b)            # 22.75
print(type(b))      # <class 'float'>

x = str(b)          # converte o float em b para string
print(x)            # 22.75
print(type(x))      # <class 'str'>
