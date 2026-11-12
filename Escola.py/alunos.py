def cadastrar_aluno():
    while True:
     try : 
        nome = str(input("Digite o nome do aluno: ").strip())

        if not nome:
            print("O nome não pode estar vazio.")
            continue
        elif "  " in nome:
            print("O nome não pode conter espaços em branco no início ou no final.")
            continue
        else:
            alunos_cadastrados.append(nome)
     except ValueError:
        print("Digite um nome valido")
     break
    return nome


alunos_cadastrados = []
