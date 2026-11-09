def cadastrar_aluno():
    nome = str(input("Digite o nome do aluno: "))
    alunos_cadastrados.append(nome)
    return nome


alunos_cadastrados = []
