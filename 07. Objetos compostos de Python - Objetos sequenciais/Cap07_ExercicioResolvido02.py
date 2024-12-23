# A CLASSE range
# Muitos textos sobre a linguagem Python fazem referência a range como sendo uma função, quando na
# verdade, segundo a documentação oficial trata-se de um tipo sequencial imutável.
# Por este motivo, neste texto será usada a expressão tipo range ao invés de função range.
# A classe range existe para produzir um objeto imutável que é uma sequência de números inteiros.
# Ela tem grande importância na implementação de vários tipos de algoritmos e seu uso é simples. Sua forma geral é esta:

# range(start, stop[, step])

# A sequência começará com o valor start e terminará com o valor stop – 1.
# Assim como no fatiamento, o valor final nunca é incluído.
# Se o objeto step for fornecido seu valor será usado como passo para construção da sequência.
# Lembre-se sempre desses detalhes:
# • O parâmetro stop é obrigatório.
# • O parâmetro start é opcional e se não for fornecido será assumido o valor padrão 0.
# • O parâmetro step é opcional e se não for fornecido será assumido o valor padrão 1.

# Alguns exemplos:
print(list(range(10)))           # gera a sequência [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(3, 8)))         # gera a sequência [3, 4, 5, 6, 7]
print(list(range(5, 12, 3)))     # gera a sequência [5, 8, 11]


# Enunciado: Usando a classe range, escreva um programa que leia três números inteiros: o primeiro termo P, a
# razão R e a quantidade Q de termos de uma progressão aritmética. O programa deve calcular os Q
# termos da progressão colocando-os em uma lista e no final exibi-la na tela.

P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Q = int(input("Digite a qtde de termos: "))
ultimo = P + R * (Q-1)
Termos = list(range(P, ultimo+1, R))        # a classe range gera a PA
print('Lista gerada com range')
print(Termos)
print('Fim do Programa')

# Digite o primeiro termo: 4
# Digite a razão: 7
# Digite a qtde de termos: 12
# Lista gerada com range
# [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81]
# Fim do Programa


# Neste exercício temos o mesmo enunciado do exercício resolvido anterior, porém a solução é diferente.
# Nela foi usada classe range para gerar a PA. Note que para usar range precisamos saber o último termo da PA desejada.
# Assim foi calculado:

# ultimo = P + R * (Q-1)

# Essa fórmula é decorrente da matemática, não exatamente um assunto de programação de computadores.
# Precisamos desse último termo se quisermos usar range, então fomos buscar na matemática a forma de calculá-lo.
# Isso ocorre sempre em programação. Muitas vezes precisamos de informações especializadas da área de conhecimento
# para a qual estamos escrevendo o programa.

# No que diz respeito ao uso do range, o código usado requer duas explicações.

# Termos = list(range(P, ultimo+1, R))

# Primeiro, note que no parâmetro stop foi usado ultimo+1. Isso é necessário pois o stop nunca está
# incluído na sequência gerada, então para garantir a inclusão do ultimo precisamos estabelecer último+1
# como stop do range.
# Segundo, note que a classe range foi colocada dentro da função de conversão list:
# ... list(range(...))
# Essa conversão da classe range para a classe list é necessária para que possamos ver os valores
# da sequência na tela. Se não for feita vemos o que está a seguir:

# Termos = range(P, ultimo+1, R)
# print(Termos)             # range(7, 52, 4)


# Não-Pythônico e Pythônico
# Aqui temos o mesmo problema com outra solução.
# Esta solução pode ser considerada mais Pythônica do que a solução anterior.
# Motivo: ela utiliza recurso específico de Python que elimina a necessidade do laço while,
# sendo mais compacta e legível.
# É disso que se trata quando mencionamos Não-Pythônico e Pythônico.
