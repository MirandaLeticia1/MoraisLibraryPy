from Biblioteca.lib.interface import *

#Função para ver se o um arquivo já existe
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#Função para criar o arquivo que irá conter o relatório
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

#Função para ler o arquivo do relatório
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler relatório')
    else:
        cabeçalho('LIVROS CADASTRADOS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print (f'OBRA:: {dado[0]:<10} TIPO {dado[1]:<10} ANO {dado[2]:<10} AUTOR {dado[3]:<10} ASSUNTO {dado[4]:>3}')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', tipo='Desconhecido', ano =0, autor='desconhecido', assunto='desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{tipo};{ano};{autor};{assunto}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} concluído com sucesso!!!')
            a.close()

def cadastrarCat(arqCat, nome='Desconhecido'):
    try:
        a = open(arqCat, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} concluído com sucesso!!!')
            a.close()

def cadastrarCTema(arqTema, nome='Desconhecido'):
    try:
        a = open(arqTema, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} concluído com sucesso!!!')
            a.close()

def buscaLivro(nome):
    with open("relatorio.txt", "r") as arq:
        mensagem = 'Livro inexistente'
        livros = ''
        for linha in arq:
            if linha.find(nome) > -1:
                livros += linha
        if livros == '':
            print(mensagem)
        else:
            print(livros)

def login(user,passw):
    f = open("usuarios.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split(";")
        if (user in us) and (passw in pw):
            print('')
            return True
    return False
