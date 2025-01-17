# Enunciado: Escreva um programa que leia do teclado o código de um produto e seu preço unitário. O código é
# um string e o preço é real. Acrescente o par código:preço em um dicionário. O laço termina quando
# for fornecido um string vazio para o código. Ao final, exibir código e preço, um produto em cada linha.

produtos = {}
print('Leitura dos dados')
cod = input('  Digite o código: ')          # lê o primeiro código
while cod != '':                            # se cod diferente de vazio segue no laço
    preco = float(input('  Digite o preço: '))      # lê o preço
    produtos[cod] = preco                           # acrescenta novo item ao dicionário
    cod = input('  Digite o código: ')              # lê o próximo cod
print('Fim da leitura dos dados\n')
print('Preço dos Produtos')
for cod in produtos.keys():                 # faz iteração como Caso 1 – usando .keys()
    print(f'  produto {cod} custa R$ {produtos[cod]:7.2f}')
print("\nFim do programa")

# Leitura dos dados
#   Digite o código: 7899099016244
#   Digite o preço: 16.9
#   Digite o código: 7899099001288
#   Digite o preço: 8.43
#   Digite o código: 7899099002544
#   Digite o preço: 166.35
#   Digite o código: 7899099006931
#   Digite o preço: 53.8
#   Digite o código:
# Fim da leitura dos dados
#
# Preço dos Produtos
#   produto 7899099016244 custa R$   16.90
#   produto 7899099001288 custa R$    8.43
#   produto 7899099002544 custa R$  166.35
#   produto 7899099006931 custa R$   53.80
#
# Fim do programa


# Neste exercício foi fornecido um código com 13 dígitos que se assemelha a um código de barras e o
# preço foi exibido formatado ocupando 7 posições de tela, com 2 casas decimais.

# Observe que nenhum cuidado foi tomado a respeito de eventual verificação se o produto já está no
# dicionário ou não. Desse modo, se o mesmo código for fornecido duas vezes com preços diferentes, o preço
# que vai prevalecer será o último. Esta questão será considerada no próximo exercício resolvido.

# Um último comentário neste exercício é sobre a lógica implementada: note que fizemos uso da técnica
# de leitura do dado de controle na saída do laço, ou seja, a leitura do código do produto é última instrução
# dentro do laço. Por consequência, a primeira leitura deve ser feita antes do laço iniciar.
