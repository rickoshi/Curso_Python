# FORMATAÇÃO USANDO f-string
# Outro modo de formatação é chamado de f-string (abreviação para "formatted string literals").
# Foi introduzido na versão 3.6 e faz o mesmo que o método .format(), porém com uma escrita mais clara e compacta.
# Um f-string começa com "f" ou "F" e dentro do marcador {} é colocado o objeto que se quer exibir naquela posição.
# Para s1 foi usado o método .format(). Para s2 foi usado o f-string obtendo-se o mesmo resultado.

A = 14
B = 32
s1 = "Valores: A é {} e B é {}".format(A, B)
s2 = f"Valores: A é {A} e B é {B}"
print(s1)       # Valores: A é 14 e B é 32
print(s2)       # Valores: A é 14 e B é 32

# Formatação com .format()              Formatação com f-string
# S = "Dado = {:d}".format(A)           S = f"Dado = {A:d}"
# S = "Dado = {:5d}".format(A)          S = f"Dado = {A:5d}"
# S = "Dado = {:f}".format(X)           S = f"Dado = {A:f}"
# S = "Dado = {:7.3f}".format(X)        S = f"Dado = {X:7.3f}"
# S = "Dado = {:.2f}".format(X)         S = f"Dado = {X:.2f}"
# S = "..{:>7d}..".format(A)            S = f"..{A:>7d}.."
# S = "..{:<7d}..".format(A)            S = f"..{A:<7d}.."
# S = "..{:^7d}..".format(A)            S = f"..{A:^7d}.."

# Existe um terceiro e antigo modo de formatação de strings em Python.
# Este modo é similar ao usado no comando printf da linguagem C e usa o
# operador de interpolação de string representado pelo caractere %.
# Ele é mantido para manter a compatibilidade com softwares que o utilizam.
