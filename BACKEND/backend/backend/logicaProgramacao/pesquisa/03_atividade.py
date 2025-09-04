while True:
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("3 - Alterar")
    print("4 - Excluir")
    print("5 - Sair")

    opcao = input("Escolha: ")

    match opcao:
        case "1":
            try:
                arq = open("usuarios.txt", "a")
                nome = input("Nome: ")
                email = input("Email: ")
                arq.write(nome + "," + email + "\n")
                arq.close()
                print("Cadastrado!")
            except:
                print("Erro no cadastro.")

        case "2":
            try:
                arq = open("usuarios.txt", "r")
                for linha in arq:
                    print(linha.strip())
                arq.close()
            except:
                print("Nenhum usuário.")

        case "3":
            try:
                nomeAntigo = input("Nome que deseja alterar: ")
                arq = open("usuarios.txt", "r")
                usuarios = arq.readlines()
                arq.close()

                arq = open("usuarios.txt", "w")
                for u in usuarios:
                    nome,email = u.strip().split(",")
                    if nome == nomeAntigo:
                        novoNome = input("Novo nome: ")
                        novoEmail = input("Novo email: ")
                        arq.write(novoNome + "," + novoEmail + "\n")
                        print("Alterado!")
                    else:
                        arq.write(u)
                arq.close()
            except:
                print("Erro ao alterar.")

        case "4":
            try:
                nomeExcluir = input("Nome que deseja excluir: ")
                arq = open("usuarios.txt", "r")
                usuarios = arq.readlines()
                arq.close()

                arq = open("usuarios.txt", "w")
                for u in usuarios:
                    nome,email = u.strip().split(",")
                    if nome != nomeExcluir:
                        arq.write(u)
                arq.close()
                print("Excluído!")
            except:
                print("Erro ao excluir.")

        case "5":
            print("Saindo...")
            break

    if opcao not in ["1","2","3","4","5"]:
        print("Opção inválida")