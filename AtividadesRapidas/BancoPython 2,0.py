# version 2.1

print("Olá, Bem vindo ao banco Python!")

nome = str(input("\nDigite seu nome "))

while True:
    try:

        conta = int(input("\nDigite sua Conta: "))
        break
    except ValueError:
        print("Digite somente numeros!")


saldo = 500.00
historico = []

while True:

    op = int(input("\nQual operação deseja realizar? \
     \n1 - Saque \
     \n2 - Deposito \
     \n3 - Consulta de valor \
     \n4 - Encerrar\
     \n5 - Consultar conta\
     \n6 - Consultar operações\
     \nOpção desejada: "))

    if op < 1 or op > 6:
        print("Opção inválida!")
    elif op == 1:
        saque = float(input("\nDiste o valor de deseja sacar: R$"))
        if saque <= 0:
            print("o valor deve ser superior a R$0.00")

        elif saque > saldo:
            print("O valor do saque é superior ao saldo atual\nOperacáo cancelada ")

        else:
            saldo = saldo - saque
            historico.append(
                f"Saque de R${saque:.2f} | Saldo restante R${saldo:.2f}")
            print("O valor sacado é de R$", saque)
            print("Seu saldo restante é de R$:", saldo)

    elif op == 3:
        print("\nO saldo da sua é de R$", saldo)

    elif op == 2:
        deposito = float(input("Digite o valor que deseja depoistar R$"))
        if deposito <= 0:
            print("O deposito deve ser maior que R$0.00\nOperacáo cancelada")
        else:
            saldo = saldo + deposito
            historico.append(
                f"Deposito no valor de R${deposito:.2f} | Saldo restante R${saldo:.2f}")
            print("\nO valor depositado é de R$", deposito, "\
            \nO saldo atual é de R$", saldo)
    elif op == 5:
        print("\nConta em nome de : ", nome)
        print("\nSeu saldo é de R$", saldo)
        print("\nSua conta é a: ", conta)
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


print("\nObrigado por usar o banco Python")
