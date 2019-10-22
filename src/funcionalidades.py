class Funcionalidades(object):
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
        self.op = int(input('Informe a opção: '))

        # verificando opção
        while self.op < 1 or self.op > 5:
            self.op = int(input('Opção INVÁLIDA! Informe a opção: '))
        print(f'-' * 50)

    def depositar(self):
        pass

    def sacar(self):
        pass

    def transferir(self):
        pass

    def pagarConta(self):
        pass
