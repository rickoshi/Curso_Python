# Enunciado: Escreva um programa para uma fábrica de calçados que leia o código LL de um calçado, que é um
# número inteiro com 2 dígitos. Exiba na tela a linha do calçado, conforme a tabela a seguir. Se o
# número fornecido não estiver na tabela, deve-se exibir a mensagem "Código inválido".

# LL    Linha de calçados   LL  Linha de calçados
# 16    Bebê                49  Masculino esportivo
# 23    Infantil feminino   52  Feminino formal salto baixo
# 25    Infantil masculino  53  Feminino formal salto alto
# 29    Infantil esportivo  55  Feminino casual salto baixo
# 42    Masculino formal    56  Feminino casual salto alto
# 43    Masculino casual    59  Feminino esportivo

LL = int(input('Digite a linha de calçados: '))
match LL:
    case 16:
        print('Bebê')
    case 23:
        print('Infantil feminino')
    case 25:
        print('Infantil masculino')
    case 29:
        print('Infantil esportivo')
    case 42:
        print('Masculino formal')
    case 43:
        print('Masculino casual')
    case 49:
        print('Masculino esportivo')
    case 52:
        print('Feminino formal salto baixo')
    case 53:
        print('Feminino formal salto alto')
    case 55:
        print('Feminino casual salto baixo')
    case 56:
        print('Feminino casual salto alto')
    case 59:
        print('Feminino esportivo')
    case _:
        print('Código fornecido é inválido')

# Digite a linha de calçados: 23
# Infantil feminino

# Digite a linha de calçados: 43
# Masculino casual

# Digite a linha de calçados: 55
# Feminino casual salto baixo

# Digite a linha de calçados: 57
# Código fornecido é inválido


# Vale mencionar que não há qualquer impedimento sobre usar o match-case em combinação com os
# outros comandos existentes em Python, como: condicional if-elif-else, laço de repetição while e
# iterador for.

# Benefícios ao utilizar match-case
# Este comando foi recebido na comunidade Python com muito entusiasmo e oferece diversos
# benefícios em termos de sintaxe e performance, incluindo:
# • Estrutura concisa: permite transformar complexas estruturas de ifs aninhados em uma forma concisa e legível.
# • Legibilidade: com sua sintaxe clara, torna o código legível e autoexplicativo.
# • Segurança: possibilita que todos os padrões possíveis sejam tratados nas cláusulas case.

# Um cuidado deve ser tomado quanto ao seu uso. Ao distribuir um script que use esse comando, poderá
# haver erro de execução do programa caso o usuário final esteja usando uma versão anterior à 3.10.
# Desse modo, seja bem claro na documentação do seu software informando ao usuário qual a versão mínima de
# Python que ele deve possuir para ser capaz de executá-lo.
# Por fim, à medida que o tempo passe essa questão será menos significativa pois a tendência é a de que
# os usuários de Python façam atualizações de suas versões.
