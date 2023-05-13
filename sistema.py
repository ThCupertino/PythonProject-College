from lib import *
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas.', 'Cadastrar nova pessoa.', 'Sair do sistema.'])
    if resposta == 1:
        #OPÇÃO DE LISTAR O CONTEÚDO DE UM ARQUIVO
        lerArquivo(arq)
    elif resposta == 2:
        #OPÇÃO DE CADASTRAR NOVA PESSOA
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Informe o nome da pessoa a ser cadastrada: ')).title()
        idade = leiaInt(f'Informe a idade de {nome}: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho(f'Encerrando o sistema. Até logo.')
        break
    else:
        print(f'\033[31mERRO. Digite uma opção válida\033[m')
    sleep(2)
