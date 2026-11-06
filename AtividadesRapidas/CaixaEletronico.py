print("Olá, Bem vindo ao banco Python!")
conta = int(input("Digite sua Conta: "))


saldo = 500.00


print("Seu saldo atual é de R$", saldo)

sacar = input("Deseja sacar ? S/N")

if sacar == "S":
    saque = float(input("Diste o valor de deseja sacar: R$"))
    if saque <= saldo:
        print("O valor sacado é de R$", saque)
        saldo = saldo - saque
        print("Seu saldo restante é de R$:", saldo)
    else:
        print("O valor do saque é superior ao saldo atual ")
elif sacar == "N":
    print("O saldo da sua conta permanece R$", saldo)
else:
    print("Digite uma opção invalida!")

print("Obrigado por usar o banco Python")
