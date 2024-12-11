# O QUE É O \n ?
# Ao usar a função print() é muito comum nos depararmos com a dupla de caracteres \n.
# Isso pode ser encontrado em várias linguagens como C, Java e Python.
# Na verdade, porém, não se trata de uma dupla de caracteres: o \n é uma "sequência de escape" (escape sequence).
# Sequências de escape consistem em uma barra invertida (\) seguida de uma letra ou dígitos e representam ações,
# como no caso do \n que representa a ação de "pulo de linha" ou "avanço de linha".

# Sempre que usado junto com print() ele faz com que o cursor de tela pule para a linha de baixo.
# Para funcionar corretamente o \n deve estar dentro das aspas

print('\n')             # pula uma linha na tela
print('um\ndois')       # escreve 'um' em uma linha, pula a linha, escreve 'dois' embaixo
print('\n\n\n')         # pula três linhas
print('\n\nAlgo')       # pula duas linhas e escreve 'Algo'

#
#
# um
# dois
#
#
#
#
#
#
# Algo
#
