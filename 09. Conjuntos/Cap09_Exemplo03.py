# CONCEITOS: HASH E HASHABLE
# Em língua portuguesa não existe uma palavra adequada para traduzir o conceito expresso pela palavra
# inglesa hash. Este é um termo que tem uso frequente no campo da tecnologia da informação, de modo que
# a hash tornou-se um neologismo, ou seja, o termo em inglês está incorporado ao português.
# O hash é um número inteiro calculado a partir do conteúdo de um objeto e existirá em memória durante
# o tempo de existência do objeto. Como esse inteiro é calculado a partir do conteúdo do objeto, dois
# objetos da mesma classe e com mesmo conteúdo terão o mesmo hash. E este é o principal propósito do
# hash: ele permite comparações rápidas entre objetos Python.
# Nem todas as classes de objetos Python podem ter o hash calculado. Apenas objetos de classes
# imutáveis tem um hash. A documentação do Python indica que um objeto é hashable se tiver um valor de
# hash que não muda durante sua vida útil. Se necessário é possível conhecer o número hash dos objetos
# Python usando a função hash(), como mostrado no exemplo a seguir.

s1 = 'texto'
print(hash(s1))     # -3800107812225830063

s2 = 'qualquer coisa'
print(hash(s2))     # -6079285544506356857

valor = 13.75
print(hash(valor))  # 1729382256910270477

x = 26
print(hash(x))      # 26

y = 26.0
print(hash(y))      # 26

t = (15, 23, 7)
print(hash(t))      # -5803187897390630569

L = [15, 23, 7]
# print(hash(l))    # TypeError: unhashable type: 'list'

# O exemplo mostra diversas situações. Observe atentamente cada uma.
# No caso de números inteiros seu hash é o próprio número.
# Números reais com a parte decimal zerada são truncados e seu hash será a
# parte inteira do número, implicando que valores numéricos como 26 e 26.0 tenham o mesmo hash.
# Tuplas são imutáveis e possuem o hash. Já as listas são mutáveis e não possuem um número hash,
# como pode ser visto pelo erro apresentado no exemplo.
