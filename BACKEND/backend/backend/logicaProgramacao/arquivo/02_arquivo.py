def gerar_lista_alunos():
    print("Seja Bem vindo, vamos cadastrar os alunos")
    print("Ao encerrar digite encerrar")

    with open("terceirao.txt", 'w') as alunos:
        while True:
            nome = input("digite o nome do aluno")
            if nome.lower() == "encerrar":
                print("encerrando cadastro")
                break
            alunos.write(nome + "\n")

gerar_lista_alunos()

def listar_alunos():
    with open("terceirao.txt", 'r') as Lista:
        print("----lista de alunos----")

        for item in Lista:
            aluno = item.strip()
            print("aluno:", aluno)

listar_alunos()