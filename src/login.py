import getpass
import users
from funcionalidades import Funcionalidades
from funcionalidades2 import Funcionalidades2


# LOGIN
def login():
    print(f'{" LOGIN ":-^50}')
    if users.user1['nome1'] == '':
        print('\033[31mNão existem usuários cadastrados!\033[m')
    else:
        while True:
            while True:
                contaLogin = input('Conta: ( xxxxx ) ').strip()
                if len(contaLogin) != 5:
                    continue
                elif contaLogin != users.user1['conta1'] and contaLogin != users.user2['conta2']:
                    print('\033[31mTHIS ACCOUNT DOES NOT EXIST!\033[m')
                    continue
                else:
                    break
            senhaLogin = getpass.getpass('Informe uma senha: ').strip()
            if contaLogin == users.user1['conta1'] and senhaLogin != users.user1['senha1']:
                print('\033[31mNÚMERO DA CONTA OU SENHA INCORRETOS!\033[m')
                continue
            elif contaLogin == users.user2['conta2'] and senhaLogin != users.user2['senha2']:
                print('\033[31mNÚMERO DA CONTA OU SENHA INCORRETOS!\033[m')
                continue
            else:
                break

        if contaLogin == users.user1['conta1'] and senhaLogin == users.user1['senha1']:
            print('\033[1;32mLogin Concluído\033[0;0m')
            print(f"\033[1;34mBem vindo {users.user1['nome1']}\033[0;0m")
            while True:
                f = Funcionalidades()
                if f.op == 1:
                    f.depositar()
                elif f.op == 2:
                    f.sacar()
                elif f.op == 3:
                    f.transferir()
                elif f.op == 4:
                    f.pagarConta()
                elif f.op == 5:
                    pass
                    break

        elif contaLogin == users.user2['conta2'] and senhaLogin == users.user2['senha2']:
            print('\033[1;32mLogin Concluído\033[0;0m')
            print(f"\033[1;34mBem vindo {users.user2['nome2']}\033[0;0m")
            while True:
                f = Funcionalidades2()
                if f.op == 1:
                    f.depositar()
                elif f.op == 2:
                    f.sacar()
                elif f.op == 3:
                    f.transferir()
                elif f.op == 4:
                    f.pagarConta()
                elif f.op == 5:
                    pass
                    break
