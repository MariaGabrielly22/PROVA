i =0
i ++ #auto incremento = automatico
inventario = []
with open("biblioteca.json", "r") as biblioteca:
    produto_para_alterar = input("Digite o ID do Produto")
    inventario = json.load(biblioteca)
    for livro in biblioteca:
        if produto_para_alterar == livro["ID"]:
            novo_nome = input("Digite o novo nome")
            livro["nome"] = novo_nome

with open("biblioteca.json", "w") as biblioteca:
    json.dump(inventario,biblioteca,indent=4)


inventario = []
with open("biblioteca.json", "r") as biblioteca:
    livro_para_excluir = input("Digite o ID do livro")
    inventario = json.load(biblioteca)
    for livro in inventario:
        novo_inventario = []
        if produto_para_alterar!= livro["ID"]:
            novo_inventario.append(livro)
           
with open("biblioteca.json", "w") as biblioteca:
    json.dump(novo_inventario,biblioteca,indent=4)



