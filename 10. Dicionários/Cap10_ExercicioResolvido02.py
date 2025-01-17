# Enunciado: Escreva um programa que leia do teclado o código de um produto e seu preço unitário. O código é
# um string e o preço é real. Acrescente o par código:preço em um dicionário. O programa deve
# verificar se o código já está no dicionário e neste caso deve emitir uma mensagem de erro. O laço
# termina quando for fornecido um string vazio para o código. Ao final, exibir código e preço, um
# produto em cada linha.

produtos = {}
print('Leitura dos dados')
while True:
    cod = input('  Digite o código: ')
    if cod == '':
        break           # interrompe o laço se cod == ''
    elif cod in produtos:
        print(f'  ...o código {cod} já está no cadastro')
        continue        # segue para a próxima iteração
    preco = float(input('  Digite o preço: '))
    produtos[cod] = preco       # acrescenta novo item ao dicionário
print('Fim da leitura dos dados\n')
print('Preço dos Produtos')
for cod in produtos.keys():
    print(f'  produto {cod} custa {produtos[cod]}')
print("\nFim do programa")

# Leitura dos dados
#   Digite o código: 7899099016240
#   Digite o preço: 16.9
#   Digite o código: 7899099001280
#   Digite o preço: 8.43
#   Digite o código: 7899099002541
#   Digite o preço: 166.35
#   Digite o código: 7899099001280
#   ...o código 7899099001280 já está no cadastro
#   Digite o código: 7899099016240
#   ...o código 7899099016240 já está no cadastro
#   Digite o código: 7899099006936
#   Digite o preço: 53.8
#   Digite o código:
# Fim da leitura dos dados
#
# Preço dos Produtos
#   produto 7899099016240 custa 16.9
#   produto 7899099001280 custa 8.43
#   produto 7899099002541 custa 166.35
#   produto 7899099006936 custa 53.8
#
# Fim do programa


# Nesta solução a forma de uso do dicionário é a mesma do exercício resolvido anterior. Porém, foi
# utilizada uma lógica bem diferente. Observe o comando while e o uso dos comandos break e continue.
# A condição do while é sempre verdadeira. Quando o código é um string vazio o comando break
# interrompe esse while. Quando o código já está no cadastro o comando continue pula o restante do
# código e segue para a próxima repetição na qual será lido um novo código.
