# Enunciado: Escreva um programa que leia dados dos Estados brasileiros: Sigla, Nome, Capital e PIB. A Sigla deve
# ser usada como chave para o dicionário e o valor deve ser uma tupla formada com (Nome, Capital,
# PIB). A leitura termina quando um string vazio for fornecido para a Sigla. Exibir os dados na tela.

UF = {}
print('Leitura dos dados')
while True:
    sigla = input('  Digite a sigla: ')
    if sigla == '':
        break       # interrompe o laço se cod == ''
    elif sigla in UF:
        print(f'  ...o código {sigla} já está no cadastro')
        continue    # segue para a próxima iteração
    estado = input('  Digite o nome: ')
    capital = input('  Digite a capital: ')
    pib = float(input('  Digite o PIB: '))
    UF[sigla] = (estado, capital, pib)      # acrescenta novo item ao dicionário
print('Fim da leitura dos dados\n')
print('     {:15} {:15} {:>10}'.format('Estado', 'Capital', 'PIB (R$ bi)'))
for sigla, dados in UF.items():
    print('({}) {:15} {:15} {:10.1f}'.format(
        sigla,
        dados[0],
        dados[1],
        dados[2])
    )
print("\nFim do programa")

# Leitura dos dados
#   Digite a sigla: AC
#   Digite o nome: Acre
#   Digite a capital: Rio Branco
#   Digite o PIB: 21.4
#   Digite a sigla: CE
#   Digite o nome: Ceará
#   Digite a capital: Fortaleza
#   Digite o PIB: 194.9
#   Digite a sigla: MT
#   Digite o nome: Mato Grosso
#   Digite a capital: Cuiabá
#   Digite o PIB: 233.4
#   Digite a sigla: PR
#   Digite o nome: Paraná
#   Digite a capital: Curitiba
#   Digite o PIB: 549.9
#   Digite a sigla: SP
#   Digite o nome: São Paulo
#   Digite a capital: São Paulo
#   Digite o PIB: 2719.8
#   Digite a sigla:
# Fim da leitura dos dados
#
#      Estado          Capital         PIB (R$ bi)
# (AC) Acre            Rio Branco            21.4
# (CE) Ceará           Fortaleza            194.9
# (MT) Mato Grosso     Cuiabá               233.4
# (PR) Paraná          Curitiba             549.9
# (SP) São Paulo       São Paulo           2719.8
#
# Fim do programa


# Acessando os dados do dicionário utilizando matrizes ao invés de duas variáveis e uma única tupla

# for item in UF.items():
#     print('({}) {:15} {:15} {:10.1f}'.format(
#         item[0],
#         item[1][0],
#         item[1][1],
#         item[1][2] )
#     )
