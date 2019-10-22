import getpass
import users
import main
from funcionalidades import Funcionalidades


def login():
    print(f'{" LOGIN ":-^50}')
    # LOGIN
    if users.user1['nome1'] == '':
        print('\033[31mNão existem usuários cadastrados!\033[m')
    else:
        while True:
            while True:
                contaLogin = input('Conta: ( xxxxx ) ').strip()
                if len(contaLogin) != 5:
                    continue
                else:
                    break
            senhaLogin = getpass.getpass('Informe uma senha: ').strip()

            if contaLogin == users.user1['conta1'] and senhaLogin == users.user1['senha1']:
                print('Login Concluído')
                print(f"Bem vindo {users.user1['nome1']}")

                f = Funcionalidades()
                if f.op == 1:
                    f.depositar()
                    break
                elif f.op == 2:
                    f.sacar()
                    break
                elif f.op == 3:
                    f.transferir()
                    break
                elif f.op == 4:
                    f.pagarConta()
                    break
                elif f.op == 5:
                    pass
                    break

            elif contaLogin == users.user2['conta2'] and senhaLogin == users.user2['senha2']:
                print('Login Concluído')
                print(f"Bem vindo {users.user2['nome2']}")

                f = Funcionalidades()
                if f.op == 1:
                    f.depositar()
                    break
                elif f.op == 2:
                    f.sacar()
                    break
                elif f.op == 3:
                    f.transferir()
                    break
                elif f.op == 4:
                    f.pagarConta()
                    break
                elif f.op == 5:
                    pass
                    break

            main.main()
