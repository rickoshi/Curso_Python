# COMANDOS CONDICIONAIS ANINHADOS
# É muito comum a necessidade de colocar um segundo comando if dentro de outro if ou else.

# O exemplo a seguir tem como enunciado: escreva um programa que forneça o tipo de
# aplicação financeira adequado a partir do grau de aceitação de risco e o valor a ser investido.
#
# Aceitação de risco    Valor < 1000,00     Valor >= 1000,00
#    Baixo (BX)            Poupança            Renda fixa
#     Alto (AL)            Bitcoins              Ações
#
# O grau de aceitação de risco deve ser lido do teclado na forma BX para baixo ou AL para alto. Se for fornecido algo
# diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido dado inválido.
# Para o valor deve-se ler um número real.

# Na solução implementada nas duas linhas iniciais foi feita a leitura dos dados de entrada.
# Em seguida um primeiro if é usado para verificar o que foi digitado para o objeto risco;
# se estiver errado, o programa exibe a mensagem e termina.

# Se estiver correto o programa segue para o else. Dentro desse else do primeiro if é escrito o resto do código.
# Um segundo if é usado para decidir se o risco é baixo ou alto.
# Em ambos os casos mais um if é usado para estabelecer o tipo de aplicação.

risco = input('Digite BX ou AL para o grau de risco: ')
valor = float(input('Digite o valor: '))
if risco != 'BX' and risco != 'AL':
    print(f'{risco} é inválido para o grau de risco')
else:
    if risco == 'BX':
        if valor < 1000.0:
            tipo = 'Poupança'
        else:
            tipo = 'Renda fixa'
    else: # risco == 'AL'
        if valor < 1000.0:
            tipo = 'Bitcoins'
        else:
            tipo = 'Ações'
    print(f'Você deve investir em {tipo}')


# primeira execução
# Digite BX ou AL para o grau de risco: AL
# Digite o valor: 2500
# Você deve investir em Ações

# segunda execução
# Digite BX ou AL para o grau de risco: AL
# Digite o valor: 500
# Você deve investir em Bitcoins

# terceira execução
# Digite BX ou AL para o grau de risco: BX
# Digite o valor: 2500
# Você deve investir em Renda Fixa

# quarta execução
# Digite BX ou AL para o grau de risco: BX
# Digite o valor: 500
# Você deve investir em Poupança

# quinta execução
# Digite BX ou AL para o grau de risco: PP
# Digite o valor: 2500
# PP é inválido para o grau de risco
