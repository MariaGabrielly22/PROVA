import json

produtos = []
categorias = []

id_categoria = 0
id_produto = 0

def carregar_arquivo(Ecommerce):
    try:
        with open(Ecommerce, 'r') as arquivo:
            dados = json.load(arquivo)
            print(f"Arquivo {Ecommerce} carregado!")
            return dados
    except FileNotFoundError:
        print(f"Arquivo não encontrado. Criando novo arquivo.")
        return []

def salvar_arquivo(nome, dados):
    with open(nome, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def exibir_menu():
    print("\n--- Gestão de E-commerce ---")
    print("1 - Cadastrar Categoria")
    print("2 - Listar Categorias")
    print("3 - Cadastrar Produto")
    print("4 - Listar Produtos")
    print("5 - Sair")

def cadastrar_categoria():
    global id_categoria
    print("Cadastrar Categoria:")
    nome_categoria = input("Nome: ").strip()
    id_categoria += 1

    armazem_categoria = {
        "nome_categoria": nome_categoria,
        "id_categoria": id_categoria
    }

    categorias.append(armazem_categoria)
    print("Categoria salva!")

def cadastrar_produto():
    global id_produto
    id_produto += 1
    nome_produto = input("Nome: ").strip()
    preco = input("Preco: ").strip()
    id_categoria_associada = input("ID da categoria associada: ").strip()

    armazem_produto = {
        "nome_produto": nome_produto,
        "id_produto": id_produto,
        "preco": preco,
        "id_categoria_associada": id_categoria_associada
    }

    produtos.append(armazem_produto)
    print("Produto salvo!")

def listar_produtos():
    print("PRODUTOS CADASTRADOS:" if produtos else "Nenhum produto cadastrado.")
    for p in produtos:
        print(f"- ID: {p['id_produto']} / Nome: {p['nome_produto']} / Preço: {p['preco']} / Categoria ID: {p['id_categoria_associada']}")

def listar_categorias():
    print("CATEGORIAS CADASTRADAS:" if categorias else "Nenhuma categoria cadastrada.")
    for c in categorias:
        print(f"- ID: {c['id_categoria']} / Nome: {c['nome_categoria']}")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        cadastrar_categoria()
    elif opcao == '2':
        listar_categorias()
    elif opcao == '3':
        cadastrar_produto()
    elif opcao == '4':
        listar_produtos()
    elif opcao == '5':
        print("Tchau! Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
