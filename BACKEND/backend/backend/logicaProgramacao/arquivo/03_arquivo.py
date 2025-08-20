def gerar_lista_convidados():
    print("Seja Bem vindo, vamos cadastrar os convidados")
    print("Ao finalizar digite fim")

    with open("convidados.txt", 'w') as convidados:
        while True:
            nome = input("digite o nome dos convidados")
            if nome.lower() == "fim":
                break
            convidados.write(nome + "\n")

gerar_lista_convidados()

def listar_convidados():
    with open("convidados.txt", 'r') as Lista:
        print("----lista de convidados----")

        for item in Lista:
            convidados = item.strip()
            print("convidados:", convidados)

listar_convidados()

def verificar_convidado():
    nome = input("Digite o nome para verificar: ")

    with open("convidados.txt", 'r') as convidados:
        lista_convidados = convidados

    if nome in lista_convidados:
        print("pode entrar")
    else:
        print("entrada negada")

verificar_convidado()