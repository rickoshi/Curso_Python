# id
# Número inteiro gerado automaticamente
# Serve para associar o objeto criado
obj1 = 10
print(type(obj1))   # <class 'int'>
print(id(obj1))     # 140714838923992

obj2 = 10
print(type(obj2))   # <class 'int'>
print(id(obj2))     # 140714835581656
# Por serem idênticos, com mesmo conteúdo e classe,
# o Python atribui ambas as variáveis a apenas um id

obj3 = 10.0
print(type(obj3))   # <class 'float'>
print(id(obj3))     # 1628706483312
# A classe float se diferencia das outras variáveis int
# Portanto, obj3 recebe outro id, diferente de obj1 e obj2
