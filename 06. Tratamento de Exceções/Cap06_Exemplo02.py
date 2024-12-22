# No exemplo a seguir existe uma lista que contém 5 elementos e houve a tentativa de exibir na tela o
# elemento de índice 10, que não existe. Como resultado ocorreu um erro da classe IndexError

L = [12, 34, 56, 67, 89]
print(L[10])

# Traceback (most recent call last):
#   File "Cap06_Exemplo02.py", line 5, in <module>
#     print(L[10])
#           ~^^^^
# IndexError: list index out of range


# Você pode estar pensando que está evidente que são erros simples e que basta atenção para não os cometer.
# Ocorre, no entanto, que as falhas nos programas do mundo real não são evidentes dessa forma.
#
# No capítulo 4 resolvemos o erro de divisão por zero com o uso de um comando condicional if.
# Então você poderia questionar: poderíamos sempre evitar os erros usando ifs? Não é tão simples assim.
# Os sistemas computacionais estão cada vez mais complexos e usar condicionais para prever e tratar
# tudo o que pode dar errado só vai fazer com que esse sistema fique cheio de condicionais e ainda mais complexo,
# pois tudo o que pode dar errado teria que ser previsto e tratado. Assim, a maioria das linguagens
# de programação possui recursos voltados para a identificação e o tratamento desses erros, cabendo ao
# profissional de programação dominar as técnicas e métodos relacionados a isso.
