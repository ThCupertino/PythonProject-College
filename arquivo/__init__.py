from arquivo import *
from lib import *
from tkinter import *
from tkinter import messagebox

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



def cadastrar(arq, tarefa='<desconhecido>', dias=0):
    try:
        a = open(arq, 'at')
    except:
        messagebox.showinfo(title=None, message=f'Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{tarefa:<30} Data limite: {dias:>5}\n')
        except:
            messagebox.showinfo(title=None, message='Houve um erro na hora de inscrever os dados.')
        else:
            messagebox.showinfo(title=None, message=f'Novo registro de {tarefa} adicionado.')
            a.close()
