# Enunciado: Escreva um programa que leia um arquivo de entrada, sabendo que esse arquivo
# tem um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela. Mostrar
# também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor.
# Usar aqui o mesmo arquivo de entrada do exercício anterior.
# Usar um iterador for e o arquivo como iterável

Lst = []
for linha in open('entrada_er_11.4.txt'):   # abre o arquivo e o usa como iterável
    Lst.append(int(linha))
print('Valores lidos do arquivo')
print(Lst)

Soma = sum(Lst)
print(f'Soma dos valores = {Soma}')
Qtde = len(Lst)
print(f'Quantidade = {Qtde}')
print(f'Média dos valores = {Soma/Qtde}')
Minimo = min(Lst)
print(f'Mínimo dos valores = {Minimo}')
Maximo = max(Lst)
print(f'Máximo dos valores = {Maximo}')
print('Fim do Programa')

# Valores lidos do arquivo
# [128, 446, 90, 363, 185, 59, 254, 148, 241, 74]
# Soma dos valores = 1988
# Quantidade = 10
# Média dos valores = 198.8
# Mínimo dos valores = 59
# Máximo dos valores = 446
# Fim do Programa


# Esta solução usa o recurso de iteração com comando for em substituição ao while da solução 11.4.
# A construção do comando for envolvendo arquivo implica na colocação da função open() como iterável do
# for. Nessa construção o objeto linha é o objeto de controle e ele receberá uma linha do arquivo por vez
# possibilitando que o programador faça qualquer processamento necessário com os dados desse string.

# for linha in open('entrada_er_11.4.txt'):
#     Lst.append(int(linha))

# Ao fazer isso não precisamos nos preocupar em fechar o arquivo, pois o iterador fará isso
# automaticamente.
# Usar esta forma é mais veloz do que o laço while no exercício anterior, pois o comando for é
# otimizado para estas situações. Essa forma é, sem dúvida, muito mais Pythônica que a anterior.
