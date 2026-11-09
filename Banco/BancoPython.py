# version 2.5

print("Olá, Bem vindo ao banco Python!")

nome = str(input("\nDigite seu nome "))

while True:
    try:

        conta = int(input("\nDigite sua Conta: "))
        break
    except ValueError:
        print("Digite somente numeros!")

saldo = 500.00


def consultar_saldo(saldo):
    print(f"Seu saldo é de R${saldo:.2f}")


def consultar_conta():
    print(f"Titular: {nome}")
    print(f"Número da conta: {conta}")


def deposito_conta(saldo, valor):
    resultado = saldo + valor
    return resultado


def saque_conta(saldo, valor):
    resultado = saldo - valor
    return resultado


def registrar_operacao(historico, operacao):
    historico.append(operacao)


historico = []

while True:
    while True:
        try:
            op = int(input("\nQual operação deseja realizar? \
                \n1 - Saque \
                \n2 - Deposito \
                \n3 - Consultar saldo \
                \n4 - Encerrar\
                \n5 - Consultar conta\
                \n6 - Consultar operações\
                \nOpção desejada: "))
            break
        except ValueError:
            print("Digite um valor númeirco")

    if op < 1 or op > 6:
        print("Opção inválida!")
    elif op == 1:
        while True:
            try:
                saque = float(input("\nDiste o valor de deseja sacar: R$"))

                if saque <= 0:
                    print("o valor deve ser superior a R$0.00")
                else:
                    break

            except ValueError:
                print("Digite um valor numerico!")

        if saque > saldo:
            print("O valor do saque é superior ao saldo atual\nOperacáo cancelada ")

        else:
            saldo = saque_conta(saldo, saque)
            registrar_operacao(
                historico, f"Saque de R${saque:.2f} | Saldo restante R${saldo:.2f}"
            )
            print("O valor sacado é de R$", saque)
            print("Seu saldo restante é de R$:", saldo)

    elif op == 3:
        consultar_saldo(saldo)
    elif op == 2:
        while True:
            try:
                deposito = float(input("Digite o valor que deseja depoistar R$"))
                if deposito <= 0:
                    print("O deposito deve ser maior que R$0.00")
                else:
                    break
            except ValueError:
                print("Digite um valor númerico!")
        saldo = deposito_conta(saldo, deposito)
        registrar_operacao(
            historico,
            f"Deposito no valor de R${deposito:.2f} | Saldo restante R${saldo:.2f}",
        )
        print("\nO valor depositado é de R$", deposito, "\
                    \nO saldo atual é de R$", saldo)
    elif op == 5:
        consultar_conta()
    elif op == 6:
        print("\nSuas operações: ")
        if len(historico) == 0:
            print("Sem operações realizadas")
        else:
            for operacao in historico:
                print(operacao)
    else:
        print("\nEstaremos encerrando as operações!")
        break

print("\nObrigado por usar o banco Python\n\n")
