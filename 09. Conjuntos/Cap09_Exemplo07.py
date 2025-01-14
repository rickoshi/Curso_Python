# CONJUNTOS USADOS COMO ITERADORES
# Os conjuntos podem ser usados como iteradores em um comando for, do mesmo modo que as
# classes de sequências. Observe bem esse exemplo. Note que o comando for foi usado duas vezes com um
# conjunto com os mesmos dados. A diferença entre eles é a ordem com que os dados foram posicionados no
# momento da criação do conjunto. Ao rodar o programa, a ordem com que os dados são exibidos na tela é a
# mesma para os dois casos. Assim este exemplo ilustra dois aspectos: primeiro mostra como que usar um
# conjunto em um laço iterador; segundo mostra que não importa qual ordem seja usada na criação do
# conjunto, uma vez inseridos no conjunto o interpretador Python decidirá em que posição cada um estará.

print("primeira execução")
conjunto = {3.3, 18.6, 34.0, 43.1, 58.7}
for c in conjunto:
    print(c)
print("\nsegunda execução")

conjunto = {18.6, 3.3, 58.7, 34.0, 43.1}
for c in conjunto:
    print(c)
print('Fim do Programa')

# primeira execução
# 34.0
# 3.3
# 18.6
# 58.7
# 43.1
#
# segunda execução
# 34.0
# 3.3
# 18.6
# 58.7
# 43.1
# Fim do Programa


# Os conjuntos em Python são uma escolha importante quando for o caso de manter uma coleção de
# elementos não repetidos e com métodos que permitam à manutenção e operações com tais elementos. No
# entanto, lembre-se de que os conjuntos não suportam indexação, ordenação ou fatiamento. E caso essas
# características sejam necessárias você deverá usar uma lista.
