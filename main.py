from Biblioteca.lib.interface import *
from Biblioteca.lib.arquivo import *
from time import sleep

arq = 'relatorio.txt'
arqCat = 'categoria.txt'
arqTema = 'tematica.txt'
arqUsuarios = 'usuarios.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

if not arquivoExiste(arqCat):
    criarArquivo(arqCat)

if not arquivoExiste(arqTema):
    criarArquivo(arqTema)

if not arquivoExiste(arqUsuarios):
    criarArquivo(arqUsuarios)

while True:
    cabeçalho('ACESSAR O SISTEMA')
    usuario = input("Usuário:")
    senha = input("Senha:")
    login(usuario,senha)

    resposta = menu(['Gerar Relatórios sobre acervo','Cadastro de novos livros', 'Buscar por exemplares', 'Cadastrar Categoria de livros', 'Cadastrar Temática de livros', 'Sair do sistema'])
    # Opção de relatório de livros

    if resposta == 1:
        print('RELATÓRIO DO ACERVO NA TELA, CONTEÚDO TAMBÉM DISPONÍVEL NO RELATÓRIO.TXT')
        lerArquivo(arq)

    #Opção para cadastrar um novo livro

    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Digite o título da obra: '))
        tipo = str(input('O livro é Físico ou Digital?: '))
        ano = int(input('Digite o ano de lançamento do livro: '))
        autor = str(input('Digite o autor do livro: '))
        assunto = str(input('Digite qual o assunto do livro'))
        cadastrar(arq, nome, tipo, ano, autor, assunto)

    #Opção para Buscar exemplares

    elif resposta == 3:

        cabeçalho('BUSCAR EXEMPLARES')
        busca = str(input("Digite o nome do livro: "))
        buscaLivro(busca)

    #Opção para cadastrar uma categoria

    elif resposta == 4:
        cabeçalho('NOVO CADASTRO DE CATEGORIA')
        cat = str(input('Digite o nome da categoria: '))
        cadastrarCat(arqCat, cat)

    # Opção para cadastrar uma temática

    elif resposta == 5:
        cabeçalho('CADASTRO DE TEMÁTICA')
        tema = str(input('Digite o nome da temática: '))
        cadastrarCat(arqTema, tema)

    elif resposta == 6:
        cabeçalho('Saindo do sistema!')
        break

    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)
