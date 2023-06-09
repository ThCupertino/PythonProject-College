from lib import *
from arquivo import *
from time import sleep
from tkinter import *
from tkinter import ttk

arq = 'tarefas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

janela = Tk()
frm = ttk.Frame(janela)
frm.grid()


def cadastro():
    telaCadastro = Tk()

    cabecalho = ttk.Label(telaCadastro, text="NOVO CADASTRO")
    cabecalho.grid(column=1, row=0)


    nomeJanela = ttk.Label(telaCadastro, text="Informe a tarefa que você deseja realizar: ")
    nomeJanela.grid(column=1, row=1, padx=25)
    inputNomeTarefa = Entry(telaCadastro, width=25)
    inputNomeTarefa.grid(column=1, row=2, padx=25)

    dataJanela = ttk.Label(telaCadastro, text=f"Informe a data limite para a terafa ser realizada: ")
    dataJanela.grid(column=1, row=3)
    inputDataTarefa = Entry(telaCadastro, width=25)
    inputDataTarefa.grid(column=1, row=4)

    enviar = Button(telaCadastro, text="Enviar", command=lambda: envio(arq, inputNomeTarefa.get(), inputDataTarefa.get()))
    enviar.grid(column=1, row=5, pady=10)

    def envio(arq, tarefa, data):
        cadastrar(arq, tarefa, data)    
        telaCadastro.destroy()

    telaCadastro.mainloop()


def mostraLista():
   tarefas = Tk()
   a = open("tarefas.txt", 'rt')
   arqTitulo = Label(tarefas, text='Pessoas Cadastradas')
   arqTitulo.grid(column=0, row=0, pady=15)
   arquivo = Label(tarefas, text=a.read())
   arquivo.grid(column=0, row=1, padx=20, pady=10)


titulo = Label(frm, text='Bem vindo ao Gerenciador de Tarefas')
titulo.grid(column=1, row=0, padx=50, pady=15)
botao = Button(frm, text="Ver tarefas atuais.", command=mostraLista)
botao.grid(column=0, row=1, padx=50)

ttk.Button(frm, text="Registrar nova tarefa.", command=cadastro).grid(column=1, row=1)

ttk.Button(frm, text="Sair", command=janela.destroy).grid(column=2, row=1, padx=50, pady=30)
janela.mainloop()
