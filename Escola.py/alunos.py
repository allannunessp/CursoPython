def cadastrar_aluno():
    while True:
     
        nome = input("Digite o nome do aluno: ").strip()

        if not nome:
            print("O nome não pode estar vazio.")
            continue
        elif "  " in nome:
            print("O nome não pode conter espaços em concecutivos.")
            continue
        else:
            alunos_cadastrados.append(nome)
        break
    return nome


alunos_cadastrados = []
