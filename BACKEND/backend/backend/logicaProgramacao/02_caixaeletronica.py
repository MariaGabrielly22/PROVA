soma = 0
valor = int(input("Digite um valor (0 para sair): "))

while valor != 0:
    opcao = input("Soma (V/F): ").upper()
    
    if opcao == "V":
        soma += valor
    else:
        soma -= valor

    valor = int(input("Digite um valor (0 para sair): "))

print("Total:", soma)
