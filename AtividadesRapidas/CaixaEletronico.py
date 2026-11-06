print("Olá, Bem vindo ao banco Python!")
conta = int(input("Digite sua Conta: "))


saldo = 500.00


print("Seu saldo atual é de R$", saldo)

op = int(input("Qual operação deseja realizar? \
     \n1 - Saque \
     \n2 - Deposito \
     \n3 - Consulta de valor \
     \n4 - Encerrar\
     \nOpção desejada: "))

if op == 1:
    saque = float(input("\nDiste o valor de deseja sacar: R$"))
    if saque <= saldo:
        print("O valor sacado é de R$", saque)
        saldo = saldo - saque
        print("Seu saldo restante é de R$:", saldo)
    else:
        print("O valor do saque é superior ao saldo atual ")
elif op == 3:
    print("\nO saldo da sua é de R$", saldo)
elif op == 2:
     deposito = float(input("Digite o valor que deseja depoistar R$"))
     saldo = saldo + deposito
     print( "\nO valor depositado é de R$",deposito ,"\nO saldo atual é de R$" , saldo)
elif op ==4:
    print ("\nEstaremos encerrando as operações!")
else:
    print("\nDigite uma opção invalida!")

print("\nObrigado por usar o banco Python")
