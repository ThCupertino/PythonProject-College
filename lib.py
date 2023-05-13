def leiaInt(i):
    while True:
        try:
            n = int(input(i))
        except (TypeError, ValueError):
            print(f'\033[31mERRO. Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mNúmero inteiro não informado.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42).upper())
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal.')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc

