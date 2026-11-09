print("\n\n Bem Vindo a escola Python")

while True:
    while True:
        try:
            opcao = int(input("\n O que deseja fazer? \
                \n 1 - Cadastrar aluno. \n 2 - Lista de Alunos \
                \n 3 - Sair \n Sua opção: "))
            break
        except ValueError:
            print("Digite uma opção valida")

    if opcao < 1 or opcao > 3:
        print("Opção inválida")
    elif opcao == 1:
        while True:
            try:
                from alunos import cadastrar_aluno

                nome = cadastrar_aluno()
                print(f"Aluno cadastrado: {nome}")
                break
            except ValueError:
                print("Digite um nome valido")
    elif opcao == 2:
        from alunos import alunos_cadastrados

        print("Os Alunos cadastrados são : ")
        for indice, aluno in enumerate(alunos_cadastrados, start=1):
            print(f"{indice}. {aluno}")
    else:
        print(" \nObrigado por usar nosso sistema")
        break
