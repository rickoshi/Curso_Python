# A CLASSE frozenset
# A classe frozenset é uma versão imutável da classe set. Em outras palavras frozenset pode ser
# usada para criação de conjuntos imutáveis, que uma vez criados não podem ter elementos adicionados ou
# removidos, mas que ainda assim suportam as operações de diferença, união, interseção e diferença
# simétrica. Para criar um frozenset é obrigatório usar o construtor da classe, o qual recebe como parâmetro
# um iterável, de modo análogo ao construtor da classe set. Isso é mostrado no exemplo a seguir:

c1 = frozenset((16, 8, 29))
print(c1)           # frozenset({16, 8, 29})
print(type(c1))     # <class 'frozenset'>
