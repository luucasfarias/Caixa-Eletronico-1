import getpass
import users
from time import sleep


def cadastro():
    n = 0
    while True:
        ###### NOME #######
        if n != 2:
            nome = input('Nome: ').strip().title()

        if n == 0 and nome not in users.user1['nome1']:
            users.user1['nome1'] = nome
            n += 1

        elif n == 1 and nome not in users.user2['nome2']:
            users.user2['nome2'] = nome
            n += 1

        ######## CONTA #########
        while True:
            conta = input('Conta: ( xxxxx ) ').strip()
            if len(conta) != 5:
                continue
            else:
                break

        while True:
            if conta in users.user1['conta1']:
                print('Esta conta já existe!')
                while True:
                    conta = input('Conta: ( xxxxx ) ').strip()
                    if len(conta) != 5:
                        continue
                    else:
                        break
                print("-" * 50)
            else:
                if users.user1['conta1'] == '':
                    users.user1['conta1'] = conta
                    break

                if users.user2['conta2'] == '':
                    users.user2['conta2'] = conta
                    break

        ####### SENHA #####
        senha = getpass.getpass('Informe uma senha: ').strip()

        if senha not in users.user1['senha1']:
            print('\033[36mUsuário cadastrado com sucesso!\033[m')
            print("-" * 50)
            users.user1['senha1'] = senha

        elif senha not in users.user2['senha2']:
            print('\033[36mUsuário cadastrado com sucesso!\033[m')
            print("-" * 50)
            users.user2['senha2'] = senha

        while True:
            c = input('Deseja cadastrar mais alguem? [S/N] ').upper().strip()
            if c not in 'SN':
                print('ERRO! ', end='')
                continue
            else:
                break
        print("-" * 50)
        if c == 'N':
            print('Saindo ...')
            sleep(1.4)
            break

        if n == 2:
            print('\033[31mLIMITE DE DADOS ATINGINDO!\033[m')
            print('Saindo ...')
            sleep(1.4)
            break
