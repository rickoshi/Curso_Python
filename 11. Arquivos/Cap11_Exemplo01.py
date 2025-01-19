# ENTENDENDO OS ARQUIVOS
# A esta altura do curso você já deve ter percebido que cresceu consideravelmente o volume de dados
# que estamos digitando e processando nos exemplos e exercícios. É natural que isso aconteça,
# principalmente após a introdução dos tópicos sobre objetos de classes estruturadas, como listas e
# dicionários. Afinal, classes assim existem exatamente para trabalhar com grandes volumes de dados.

# Por outro lado, cada programa que fizemos até o momento exige que todos os dados sejam digitados,
# em seguida são processados e por fim os resultados exibidos em tela. Ao término do programa eles são
# perdidos, pois estavam apenas na memória do computador, não tendo sido salvos em lugar algum.
# Deste modo, está na hora de aprender algum recurso que permita o salvamento de dados e por
# consequência, permita também a leitura deles quando necessário.

# Existem basicamente duas tecnologias para salvamento e recuperação de dados: os Arquivos e os
# Sistemas Gerenciadores de Bancos de Dados (SGBD). Neste capítulo vamos aprender a trabalhar com
# Arquivos em Python.

# Um arquivo de computador é um recurso de armazenamento de dados disponível em todos os tipos de
# dispositivos digitais, sejam computadores de qualquer porte ou dispositivos móveis. Para cumprir o objetivo
# de tornar permanente o armazenamento dos dados, os arquivos devem ser gravados em algum equipamento
# físico que não dependa de um suprimento constante de energia. Atualmente os equipamentos (hardware)
# mais usados para isto são os discos magnéticos e os dispositivos dotados de memória flash (SSD).

# Em todos os sistemas computacionais quem fica responsável pelo acesso, gravação e leitura nos
# dispositivos físicos é o software básico, ou Sistema Operacional. Isso garante maior segurança, padronização
# e organização das unidades de armazenamento.

# As linguagens de programação, por sua vez, são dotadas de comandos para realizar as operações com
# arquivos, mas dependem do Sistema Operacional para executar as operações no hardware. Assim, os
# comandos existentes nas linguagens tem o papel de acionar as funções de arquivos previstas no Sistema Operacional.
# Esta forma de colaboração entre linguagem de programação e Sistema Operacional traz uma
# grande vantagem aos programadores, pois não precisam conhecer os muitos detalhes que envolvem as
# operações de acesso ao hardware para executar a tarefa de leitura e gravação de um arquivo.

# Se tivéssemos condição de "olhar" um arquivo gravado no disco "veríamos", na prática, uma coleção
# de bytes rotulada com um nome. Os bytes do arquivo representam os dados de seu conteúdo. Quando esses
# bytes são lidos eles podem ser interpretados da maneira que quisermos, mas há necessidade de que essa
# interpretação seja adequada. Por exemplo, se os bytes gravados representam dados de uma imagem no
# formato .png e ao fazer a leitura você os interpretar como dados de uma música .mp3 vai dar tudo errado e,
# no máximo você ouvirá ruído.
# Deste modo, ao ler um arquivo do dispositivo você precisa conhecer sua natureza, ou, a estrutura dos
# seus bytes. Falando sobre essa estrutura do arquivo saiba que há duas categorias essenciais: os arquivos
# texto e os arquivos binários.


# Arquivos texto
# Nos arquivos texto os bytes representam caracteres legíveis. Esse tipo de arquivo é muito usado para
# gravação de coisas como: código fonte de programas; arquivos HTML e CSS de páginas web; arquivos XML e
# CSV (comma separated values) usados para intercâmbio de dados entre sistemas; arquivos TXT em geral. Em
# termos práticos, qualquer arquivo texto pode ser diretamente aberto e lido em programas como o Bloco de Notas
# do Windows ou o Notepadqq do Linux.

# Arquivos binários
# Os arquivos binários, por sua vez, ao serem abertos e lidos devem ter seus bytes devidamente
# interpretados. Como exemplo de arquivos binários comuns temos vários tipos: imagens, áudio, vídeo, bancos
# de dados, programas executáveis compilados, arquivos compactados através de um algoritmo de
# compressão, etc. Cada um desses tipos tem formato próprio para os bytes e esse formato deve ser
# considerado e interpretado no momento da leitura.
# Para quem está começando em programação, trabalhar diretamente com os bytes de arquivos binários
# é mais complicado, devido a essa multiplicidade de formatos existentes.


# CODIFICAÇÃO DE ARQUIVOS TEXTO
# Os arquivos texto são bem mais simples que os arquivos binários, mas eles também existem em
# diferentes versões. Precisamos conhecer o que é denominado "codificação do arquivo texto".
# A base dessa codificação são as tabelas de caracteres.

# A memória do computador comporta apenas bits 0 e 1. Grupos de 8 bits formam 1 byte. Bits e bytes,
# porém, são informações de natureza numérica e precisamos de alguma forma de estabelecer uma relação
# entre o número inteiro de um byte e letras, algarismos e sinais de pontuação como 'A', 'B', 'a', 'b', '0', '1',
# '+', '*', ou qualquer outro.

# Para isso foram criadas tabelas de correspondência entre números inteiros e caracteres.
# Historicamente a primeira dessas tabelas foi a "Tabela ASCII" (American Standard Code for Information
# Interchange). Mas essa tabela é limitada pois permite a codificação de apenas 256 caracteres, em seu limite
# máximo – que é o limite de combinações para 1 byte.

# Quando os sistemas computacionais estavam restritos ao idioma inglês a tabela ASCII supria as
# necessidades. Com o tempo surgiu a necessidade de suportar outros idiomas nos sistemas computacionais,
# como o português ('é', 'É', 'á', 'ô', 'Â', 'ç', 'Ç', etc); todos os idiomas latinos; os alfabetos grego,
# cirílico, árabe; os idiomas japonês, chinês, coreano; e isso é só uma parte.
# Para suprir toda essa gama de idiomas foi criado o padrão Unicode.

# Do padrão Unicode deriva um outro padrão denominado UTF-8 que é muito usado nos idiomas de
# origem latina e comporta todos os caracteres acentuados que eles contém (essa definição não é perfeita,
# mas atende às nossas necessidades neste texto).

# Assim, nossos arquivos texto estarão codificados ou como ASCII ou como UTF-8.

# Esse assunto é extenso e recheado de detalhes que não cabem no escopo deste texto, porém o que
# precisamos saber é que para trabalharmos com arquivos texto em Python precisaremos usar a codificação
# certa. Sobre isso existem duas situações:
# • No momento da gravação do arquivo: precisamos escolher uma codificação para gravar;
# • No momento da leitura do arquivo: precisamos saber com qual codificação ele foi gravado e fazer
# a leitura usando a codificação certa.

# No momento da leitura, se usarmos a codificação errada pode acontecer do programa dar erro e ser
# interrompido ou de termos os caracteres errados na memória.


# ABERTURA E FECHAMENTO DO ARQUIVO
# Para ler ou gravar arquivos a primeira tarefa é abri-lo. Em Python, para abrir um arquivo deve-se utilizar
# a função open que contém diversos parâmetros como mostrado a seguir. O único parâmetro obrigatório é o
# nome do arquivo. Além do nome, os parâmetros do nosso interesse são modo e encoding.

# arquivo = open(nome, modo, buffering, encoding, errors, newline, closefd, opener)

# O retorno da função open pode ser atribuído a um objeto. No caso acima usamos o identificador
# arquivo.


# Parâmetro nome
# Neste parâmetro passamos o nome do arquivo. Esse nome deve seguir as regras de nomes de arquivos
# do sistema operacional onde o programa será executado, podendo incluir a letra do dispositivo e nomes de
# pastas e subpastas onde será gravado. Se dispositivo e pasta não estiverem presentes o arquivo será gravado
# na mesma pasta onde está o programa.


# Parâmetro modo
# Este parâmetro define qual a finalidade da abertura do arquivo conforme o quadro a seguir:

# Grupo     Caractere   Significado
# G1        r           Abre para leitura. Esta opção é padrão e será assumida se nada for especificado.
#           w           Abre para escrita, eliminando o seu conteúdo (não haverá pedido de confirmação).
#           x           Abre para criação exclusiva. S o arquivo já existir o comando gera um erro.
#           a           Abre para escrita, e caso o arquivo já exista mantém seu conteúdo e anexa novos dados ao final.

# G2        b           Abre o arquivo no modo binário.
#           t           Abre o arquivo no modo texto. Esta opção é padrão e será assumida se nada for especificado.
#           +           Aberto para atualização. Permite leitura e escrita concomitantes.

# Grupo 1
# Os modos do grupo 1 são mutuamente exclusivos, ou seja, você deve escolher um deles.
# Se nenhum for especificado r é o padrão.

# Grupo2
# Os modos do grupo 2 são mutuamente exclusivos – b para arquivos binários e t para arquivos texto.
# Se nenhum for especificado t é o padrão.

# Opção +
# Ao usar essa opção você poderá ler e gravar no arquivo na mesma operação de abertura.


# Parâmetro encoding
# Este parâmetro só se aplica a arquivos texto.
# As duas opções frequentemente usadas nos idiomas latinos são 'ANSI' e 'UTF-8', escritas
# exatamente dessa forma, em letras maiúsculas.


# Demais parâmetros
# Os demais parâmetros – buffering, errors, newline, closefd, opener – fogem ao escopo
# deste texto, bastando dizer que seus valores padrão atendem às necessidades dos nossos exemplos e
# exercícios.


# Em qualquer linguagem de programação
# arquivos sempre devem ser abertos, usados e fechados.
# Não esqueça de fechar, pois pode resultar em arquivo corrompido.

# Terminado o trabalho com um arquivo é preciso fechá-lo. Isso é feito com o método .close().
# arquivo.close()


# MÉTODOS DOS OBJETOS DE ARQUIVO
# A classe que define arquivos em Python tem o nome"_.io.TextIOWrapper". O quadro a seguir mostra
# os métodos mais usados dessa classe.

# Método            Descrição
# .close()          Fecha o arquivo que foi aberto com open.
#                   Se o arquivo está aberto para gravação, primeiro descarrega seu buffer.
# .flush()          Descarrega o buffer de um arquivo aberto para gravação, sem fechá-lo.
# .read(tamanho)    Lê e retorna a quantidade tamanho de caracteres. Se tamanho for negativo ou None lê
#                   todos os caracteres do arquivo.
# .readline()       Lê uma linha do arquivo e avança o cursor para o início da próxima. Retorna um string com
#                   o conteúdo da linha, incluindo o caractere '\n' no final se ele estiver presente no arquivo.
# .readlines()      Lê todas as linhas do arquivo e retorna-as como uma lista de strings, incluindo o '\n' no
#                   final de cada uma. É preciso ter cuidado com essa opção no caso de arquivos muito
#                   grandes.
# .write(dados)     Grava no arquivo o string dados. É obrigatório que dados seja da classe string.
# .writelines(lst)  Grava no arquivo todos os strings contidos na lista lst.
