# Alternativamente, pode-se criar o dicionário vazio e acrescentar os elementos como mostrado no
# exemplo a seguir:

UF = {}
print(type(UF))             # <class 'dict'>
print(UF)                   # {}
UF['SP'] = 'São Paulo'
UF['RJ'] = 'Rio de Janeiro'
UF['MG'] = 'Minas Gerais'
print(UF)                   # {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais'}
