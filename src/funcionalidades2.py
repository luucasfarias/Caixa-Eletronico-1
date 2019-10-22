from time import sleep
import users


class Funcionalidades2(object):
    op = 0

    def __init__(self):
        global op
        print(f'{" OPÇÕES ":-^50}')

        print('''[ 1 ] Depositar
[ 2 ] Sacar
[ 3 ] Transferir
[ 4 ] Pagar Conta
[ 5 ] Sair''')

        # informando a opção escolhida
        print("-" * 50)
        self.op = int(input('Informe a opção: '))

        # verificando opção
        while self.op < 1 or self.op > 5:
            self.op = int(input('Opção INVÁLIDA! Informe a opção: '))

    # DEPOSITO
    def depositar(self):

        saldo = 0
        # pedindo o saldo
        quant = float(input('Informe a quantia a ser depositada: R$'))

        # verificando quantia
        while quant <= 0:
            quant = float(input('Valor INVÁLIDO! Tente Novamente: R$'))
        print(f'-' * 50)

        # adicionando a quantia no saldo
        saldo += quant
        users.user2['saldo2'] += saldo

        # frescuras do print
        print('Depositando ...')
        sleep(1.2)
        print(f'Você depositou R$\033[1;32m{quant:.2f}\033[0;0m')
        print(f"Seu saldo atual é de R$\033[1;32m{users.user2['saldo2']:.2f}\033[0;0m")

    # SACAR
    def sacar(self):
        if users.user2['saldo2'] == 0:
            print('Para fazer o saque é preciso ter saldo na conta!')
            print(f"Seu saldo atual é de R$\033[1;32m{users.user2['saldo2']:.2f}\033[0;0m")
            print(f'-' * 50)
        else:
            # pedindo o valor de saque
            valor = float(input('Valor a ser retirado: R$'))

            # verificando valor
            while valor <= 0:
                valor = float(input('Valor INVÁLIDO! Tente Novamente: R$'))
            print(f'-' * 50)

            if valor > users.user2['saldo2']:
                print('Não foi possível completar a operação!\nO valor do saque é maior do que seu saldo!')
            else:
                # removendo o valor do saldo
                users.user2['saldo2'] -= valor
                # frescuras do print
                print('Retirando ...')
                sleep(1.2)
                print(f'Você retirou R$\033[1;32m{valor:.2f}\033[0;0m')
                print(f"Seu saldo atual é de R$\033[1;32m{users.user2['saldo2']:.2f}\033[0;0m")

    def transferir(self):
        while True:
            while True:
                contaTransferencia = str(input('Conta: (xxxxx) ')).strip()
                if len(contaTransferencia) != 5:
                    continue
                else:
                    break

            if contaTransferencia == users.user1['conta1']:
                sleep(1)
                print('Adicionando ...')
                sleep(1.2)
                print('Conta adicionada com sucesso!')
                print(f'-' * 50)

                valorTransferencia = float(input('Informe o valor a ser transferido: R$'))
                while valorTransferencia <= 0:
                    valorTransferencia = float(input('Valor INVÁLIDO! Tente Novamente: R$'))

                print(f'-' * 50)

                if valorTransferencia > users.user2['saldo2']:
                    print('Não foi possível completar a operação!\nO valor da tranferência é maior do que seu saldo!')
                else:
                    users.user2['saldo2'] -= valorTransferencia
                    users.user1['saldo1'] += valorTransferencia
                    sleep(1)
                    print('Transferindo ...')
                    sleep(1.2)
                    print('Transferencia concluída com sucesso!')
                    print(f"Você transferiu R${valorTransferencia:.2f} para {users.user1['nome1']}!")
                    print(f"Seu saldo atual é de R${users.user2['saldo2']:.2f}!")
                break
            else:
                print('Esta conta não está cadastrada!')
                continue

    # PAGANDO CONTA
    def pagarConta(self):
        codigo = str(input('Informe o código de barra da conta: (xxxxx) ')).strip()

        while True:
            if len(codigo) != 5:
                codigo = str(input('Informe um código de barra válido: (xxxxx) ')).strip()
            else:
                break

        print('Adicionando ...')
        sleep(1)
        print('Conta adicionada com sucesso!')

        valorConta = float(input('Informe o valor da conta: R$'))
        while valorConta <= 0:
            valorConta = float(input('Valor INVÁLIDO! Tente Novamente: R$'))

        print(f'-' * 50)

        if valorConta > users.user2['saldo2']:
            print('Não foi possível completar a operação!\nO valor da conta é maior do que seu saldo!')
        else:
            users.user2['saldo2'] -= valorConta
            sleep(1)
            print('Pagando ...')
            sleep(1.2)
            print('Pagamento concluída com sucesso!')
            print(f'Total pago: R${valorConta:.2f}!')
            print(f"Seu saldo atual é de R${users.user2['saldo2']:.2f}!")
