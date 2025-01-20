# Enunciado: Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos
# os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com
# três casas decimais. Usar o método .writelines()

Lst = []
A = float(input('Digite um real: '))
while A != 0:
    Lst.append(f'{A:.3f}\n')
    A = float(input('Digite um real: '))
arq = open('saida_er_11.3.txt', 'w')        # abre o arquivos para gravação
arq.writelines(Lst)                         # grava toda a lista em linhas de arquivo
arq.close()                                 # fecha o arquivos
print('Fim do Programa')

# Digite um real: 7.32
# Digite um real: 18.6
# Digite um real: 0.414
# Digite um real: 16.379
# Digite um real: 0
# Fim do Programa


# Utilizando um print(Lst) em cada laço, vemos como os valores são armazenados:
# Digite um real: 7.32
# ['7.320\n']
# Digite um real: 18.6
# ['7.320\n', '18.600\n']
# Digite um real: 0.414
# ['7.320\n', '18.600\n', '0.414\n']
# Digite um real: 16.379
# ['7.320\n', '18.600\n', '0.414\n', '16.379\n']
# Digite um real: 0
# Fim do Programa


# Neste caso os mesmos dados foram digitados e o resultado quanto à gravação do arquivo é exatamente
# o mesmo. A diferença está na solução. Nas soluções anteriores o arquivo foi aberto no início
# do programa e permaneceu aberto durante o laço. Nesta nova solução o arquivo é aberto
# apenas no momento da gravação, sem que seja necessário aguardar o processamento do laço. Em muitos
# casos essa estratégia é interessante e desejável, ou seja, os dados são coletados e processados e quando
# estiverem prontos são gravados todos de uma vez, numa única operação.
