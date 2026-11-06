print("Olá, Bem vindo ao banco Python!")
conta = int(input("\nDigite sua Conta: "))


saldo = 500.00

while True :

     op = int(input("\nQual operação deseja realizar? \
     \n1 - Saque \
     \n2 - Deposito \
     \n3 - Consulta de valor \
     \n4 - Encerrar\
     \nOpção desejada: "))

     if op == 1:
         saque = float(input("\nDiste o valor de deseja sacar: R$"))
         if saque <= 0: 
             print("o valor deve ser superior a R$0.00")

         elif saque > saldo:
             print("O valor sacado é de R$", saque)
             saldo = saldo - saque
             print("Seu saldo restante é de R$:", saldo)
         else:
             print("O valor do saque é superior ao saldo atual\nOperacáo cancelada ")
     elif op == 3:
         print("\nO saldo da sua é de R$", saldo)
     elif op == 2:
         deposito = float(input("Digite o valor que deseja depoistar R$"))
         if deposito <= 0 :
             print("O deposito deve ser maior que R$0.00\nOperacáo cancelada")
         else:
             saldo = saldo + deposito
             print( "\nO valor depositado é de R$",deposito ,"\nO saldo atual é de R$" , saldo)
     elif op ==4:
         print ("\nEstaremos encerrando as operações!")
         break
     else:
         print("\nDigite uma opção invalida!")

print("\nObrigado por usar o banco Python")
