# Enunciado: Escreva um programa para exibir na tela o nome e a categoria de um lutador.
# O programa deve ler um string para o nome e um número real para o peso.
# Conforme o peso ocorrerá o enquadramento na categoria, segundo a tabela (fictícia):

Nome = input('Digite o nome: ')
Peso = float(input('Digite o peso: '))
if Peso < 52:
    Categoria = ''
elif Peso < 65:
    Categoria = 'Pena'
elif Peso < 72:
    Categoria = 'Leve'
elif Peso < 79:
    Categoria = 'Ligeiro'
elif Peso < 86:
    Categoria = 'Meio-médio'
elif Peso < 93:
    Categoria = 'Médio'
elif Peso < 100:
    Categoria = 'Meio-pesado'
else:
    Categoria = 'Pesado'
msg = 'O lutador {} pesa {:.3f} kg e se enquadra na categoria {}'
if Categoria != '':
    print(msg.format(Nome, Peso, Categoria))
else:
    print(f'Peso inválido: {Peso}')
print("Fim do programa")

# primeira execução
# Digite o nome: Carlos
# Digite o peso: 53.9
# O lutador Carlos pesa 53.900 kg e se enquadra na categoria Pena
# Fim do programa

# segunda execução
# Digite o nome: Felipe
# Digite o peso: 43.2
# Peso inválido: 43.2
# Fim do programa

# terceira execução
# Digite o nome: Maguila
# Digite o peso: 102.3
# O lutador Maguila pesa 102.300 kg e se enquadra na categoria Pesado
# Fim do programa
