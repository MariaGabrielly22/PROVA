produtos = []

def cadastrar():
    produto = input("Nome do produto: ")
    produtos.append(produto)
    print("Ok")

def excluir():
    produto = input("Excluir produto: ")
    if produto in produtos:
        produtos.remove(produto)
        print("Ok")
    else:
        print("Excluido")

def listar():
    print("Lista dos produtos:", produtos)

opcao = ""
while opcao != "4":
    print("\nㅤMENU DE PRODUTOㅤ")
    print("1. Cadastrar")
    print("2. Excluir")
    print("3. Listar")
    print("4. Sair")
   

    opcao = input("Opcao: ").upper()

    match opcao:
        case "1":
            cadastrar()
        case "2":
            excluir()
        case "3":
            listar()
        case "4":
            print("tchau tchau")
            break
        case _:
            print("Invalido")