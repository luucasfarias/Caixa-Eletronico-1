# importando funcionalidades
from time import sleep
import cadastro
import users
import login


def principal():
    while True:
        print(f'{" BLUE-BANK ":-^50}')

        # menu principal
        print('''[ 1 ] Cadastrar Novo Cliente
[ 2 ] Listar Clientes
[ 3 ] Acessar Contas
[ 4 ] Sair''')

        print("-" * 50)
        opc = int(input('Informe a opção: '))

        #  cadastro
        if opc == 1:
            cadastro.cadastro()

        # LISTANDO USUÁRIOS
        elif opc == 2:
            users.listaUsers()

        # ACESSANDO CONTAS
        elif opc == 3:
            login.login()

        elif opc == 4:
            print('Tchau')
            break


principal()
