# COMANDO CONDICIONAL – FORMA COMPLETA
# Agora que já vimos as condições em detalhes vamos retomar as explicações sobre o comando condicional.
# if <condição 1>:
#   <bloco de comandos 1>
# elif <condição 2>:
#   <bloco de comandos 2>
# elif <condição 3>:
#   <bloco de comandos 3>
# ...
# else:
#   <bloco de comandos do else>

# A parte elif possibilita o uso de múltiplos critérios de decisão ao permitir que condições adicionais sejam usadas.
# A execução deste comando segue a seguinte lógica:
# • avaliação da <condição 1> e se ela for verdadeira será executado o <bloco de comandos 1> e pulam-se todos os demais;
# • caso a <condição 1> seja falsa, passa-se para a avaliação da <condição 2> e se ela for verdadeira
# será executado o <bloco de comandos 2>, pulando-se os demais;
# • caso a <condição 2> seja falsa, passa-se para a avaliação da <condição 3> e se ela for verdadeira
# será executado o <bloco de comandos 3>, pulando-se os demais;
# • e assim segue-se sucessivamente.
# • ao final, se nenhuma das condições postas for verdadeira, então executa-se o <bloco de comandos do else>.

# Essa é a forma completa do comando.
# Porém, as partes elif e else são opcionais e o programador poderá omiti-las caso não necessite delas.
# Quanto a quantidade de elif a serem usados, não há limite.
# Assim, o programador pode inserir tantos quantos forem necessários para implementar seu programa.

PH = float(input("Digite um valor do PH: "))
if PH < 6.0:
    r = "ácida"
elif PH < 7.0:
    r = "levemente ácida"
elif PH == 7.0:
    r = "neutra"
elif PH < 8.0:
    r = "levemente alcalina"
else:
    r = " alcalina"
print(f'Com pH = {PH} a solução é {r}')

# Digite um valor do PH: 5.8
# Com pH = 5.8 a solução é ácida

# Digite um valor do PH: 6.3
# Com pH = 6.3 a solução é levemente ácida

# Digite um valor do PH: 7
# Com pH = 7.0 a solução é neutra

# Digite um valor do PH: 7.9
# Com pH = 7.9 a solução é levemente alcalina

# Digite um valor do PH: 8.0
# Com pH = 8.0 a solução é  alcalina

# Digite um valor do PH: 8.5
# Com pH = 8.5 a solução é  alcalina
