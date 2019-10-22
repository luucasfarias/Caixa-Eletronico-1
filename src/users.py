from time import sleep

##### dicionários com usuários ######
user1 = {
    'nome1': '',
    'conta1': '',
    'senha1': '',
    'saldo1': 0
}
user2 = {
    'nome2': '',
    'conta2': '',
    'senha2': '',
    'saldo2': 0
}


def listaUsers():
    if user1['nome1'] != '' and user2['nome2'] != '':
        print('Carregando ...')
        sleep(1.2)
        print("-" * 50)
        print(f'Usuário 1: {user1["nome1"]}')
        print(f'Conta 1: {user1["conta1"]}')
        print(f'Saldo 1: R$\033[1;32m{user1["saldo1"]}\033[0;0m')
        print("-" * 50)
        print(f'Usuário 2: {user2["nome2"]}')
        print(f'Conta 2: {user2["conta2"]}')
        print(f'Saldo 2: R$\033[1;32m{user2["saldo2"]}\033[0;0m')

    elif user1['nome1'] == '':
        print('\033[31mNão existem usuários cadastrados!\033[m')

    elif user2['nome2'] == '':
        print("-" * 50)
        print('Carregando ...')
        sleep(1.2)
        print("-" * 50)
        print(f'Usuário 1: {user1["nome1"]}')
        print(f'Conta 1: {user1["conta1"]}')
        print(f'Saldo 1: R$\033[1;32m{user1["saldo1"]}\033[0;0m')
