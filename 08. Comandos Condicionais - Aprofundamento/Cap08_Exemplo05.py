# RETORNO DE VALOR
# Adicionalmente precisamos acrescentar que o if de única linha tem uma característica que é de muito
# interesse para a escrita de código compacto e legível: essa forma de if produz um retorno de valor, ou seja,
# você pode escrever uma linha de código com a seguinte forma:

# <objeto> = <comando para verdadeiro> if <condição> else <comando para falso>

# Ao usar este recurso o objeto será carregado com o retorno deste if, seja ele qual for em função da
# condição ser verdadeira ou falsa.

X = int(input('Digite um inteiro: '))
paridade = 'par' if X % 2 == 0 else 'ímpar'
print(f'O valor {X} é {paridade}')

# # primeira execução
# Digite um inteiro: 10
# O valor 10 é par

# # segunda execução
# Digite um inteiro: 11
# O valor 11 é ímpar


# Esse exemplo lê um número inteiro e mostra na tela se ele é par ou ímpar. Para determinar a paridade
# foi feito um if de única linha que retorna o string 'par' caso X seja par; caso contrário ele retorna o string
# 'ímpar'. Depois de avaliar a condição o resultado é carregado no objeto paridade, que em seguida é usado no
# print para exibição na tela.

# CONCLUSÃO SOBRE COMANDOS CONDICIONAIS EM PYTHON
# Em síntese, agora você já sabe que na linguagem Python estão disponíveis três alternativas de comando condicional.
# • Condicional clássico no formato if-elif-else;
# • Condicional múltiplo por correspondência de padrões no formato match-case;
# • Condicional de única linha;
# Você tem esses elementos da linguagem à sua disposição para escrever seus programas e pode
# escolher aquele que melhor se adeque a cada situação que ocorra em seus programas, por isso convém
# conhecê-los e saber aplicá-los às variadas situações que surgem no desenvolvimento de software.
