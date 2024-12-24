# O exemplo a seguir ilustra uma situação muito comum, em que vários valores que são digitados em uma única
# linha, devem ser lidos e separados.
# A ideia é que o usuário possa digitar algo assim:
# Digite dois inteiros e um real: 53 18 37.9
# Após a leitura queremos que o valor 53 esteja em um objeto A, o 18 esteja em B e o 37.9 esteja em X.
# A solução para isso está neste exemplo:

S = input('Digite dois inteiros e um real: ')
L = S.split()           # Faz a separação usando espaço em branco como separador
print("lista L: ", L)   # Exibe na tela a lista L
A = int(L[0])           # converte o elemento L[0] para inteiro
B = int(L[1])           # converte o elemento L[1] para inteiro
X = float(L[2])         # converte o elemento L[2] para real
print(f'A = {A}, B = {B}, X = {X}')

# Digite dois inteiros e um real: 53 18 37.9
# lista L: ['53', '18', '37.9']
# A = 53, B = 18, X = 37.9


# Adiante neste curso teremos vários usos para objetos da classe str e seus métodos. À medida que
# precisarmos de algo que ainda não foi abordado faremos uma explicação específica e demonstração de uso.
