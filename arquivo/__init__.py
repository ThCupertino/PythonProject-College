from ex115.lib import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(F'Houve um erro na criação do arquivo.')
    else:
        print(F'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Erro ao ler o arquivo.')
    else:
        cabeçalho('Pessoas Cadastradas')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome:<30}{idade:>5} anos\n')
        except:
            print(f'Houve um erro na hora de inscrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

