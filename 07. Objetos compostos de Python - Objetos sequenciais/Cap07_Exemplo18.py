# STRINGS – CLASSE str
# A classe string é a terceira na categoria das sequências. É uma classe ao mesmo tempo simples e muito
# importante, pois é muito usada. Afinal, sequências de texto estão presentes em todos os programas que você
# possa imaginar escrever, basta constatar que já estamos usando strings desde o primeiro exemplo.
# O quadro a seguir elenca os métodos de uso mais frequente da classe string.

# Método                        Descrição
# .capitalize()                 Retorna um string com a primeira letra maiúscula e as demais minúsculas, sem
#                               afetar os demais caracteres.

# .count(sub, start, end)       Conta quantas vezes um substring sub ocorre dentro do string. Se start e end
#                               forem especificados considera apenas os caracteres nesse intervalo.

# .find(sub, start, end)        Pesquisa o substring sub dentro da string e retorna um número inteiro
#                               indicando a posição se o encontrar, ou -1 caso não encontre. Se start e end
#                               forem especificados considera apenas os caracteres nesse intervalo.

# .join(iteravel)               Concatena qualquer número de elementos passados no iteravel

# .isalnum()                    Retorna True caso o string contenha apenas letras e números. Caso contrário,
#                               retorna False.

# .isalpha()                    Retorna True caso o string contenha apenas letras. Caso contrário,
#                               retorna False.

# .isnumeric()                  Retorna True caso o string contenha apenas algarismos. Caso contrário, retorna False.
#                               Útil para testar apenas dados numéricos foram digitados.

# .lower()                      Retorna um string com todas as letras minúsculas e não afeta os demais caracteres.

# .lstrip()                     Remove espaços em branco do início (lado esquerdo) do string. Também
#                               remove caracteres '\n' se presentes.
#                               Aqui vale a mesma observação feita para .strip()

# .partition(sep)               Pesquisa o string em busca do substring sub. Caso o encontre retorna três
#                               strings: a parte antes de sub, o próprio substring sub e a parte depois de sub.
#                               Caso não o encontre retorna o próprio string mais dois strings vazios.

# .replace(old, new, count)     Procura o substring old e o substitui pelo substring new. Se count for
#                               fornecido, apenas as primeiras count ocorrências são substituídas.

# .rstrip()                     Remove espaços em branco do final (lado direito) do string. Também remove
#                               caracteres '\n' se presentes.
#                               Aqui vale a mesma observação feita para .strip()

# .split(sep)                   Quebra um string em partes, usando sep como delimitador entre as partes.
#                               Retorna uma lista de strings com as partes. O delimitador sep não é incluído
#                               nas partes. Se sep não for fornecido o método usará um espaço em branco
#                               como delimitador.

# .strip()                      Remove espaços em branco do início e do final do string. Também remove
#                               caracteres '\n' se presentes.
#                               obs: Este método é um pouco mais elaborado que isso. Consulte a
#                               documentação para mais detalhes.

# .swapcase()                   Retorna um string invertendo as letras maiúsculas e minúsculas e não afeta os
#                               demais caracteres.

# .title()                      Retorna um string com a primeira de cada palavra em letra maiúscula e as
#                               demais minúsculas. Não afeta os demais caracteres.

# .upper()                      Retorna um string com todas as letras maiúsculas e não afeta os demais
#                               caracteres.


# O exemplo a seguir ilustra o uso do método .isnumeric() para validar uma entrada via teclado.
# É uma forma de evitar erros de digitação de números inteiros.

S = input('Digite um número inteiro: ')
if S.isnumeric():
    N = int(S)
    print(f' o número digitado foi {N}')
else:
    print(' Erro: digite apenas números')

# primeira execução
# Digite um número inteiro: 188
# o número digitado foi 188

# segunda execução
# Digite um número inteiro: 13abc9
#  Erro: digite apenas números
