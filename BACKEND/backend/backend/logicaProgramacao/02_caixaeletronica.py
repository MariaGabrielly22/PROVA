soma = 0

while True:
    valor = int(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break #sai do loop
    
    opcao = input("Soma (V/F): ").upper()
    
    if opcao == "V":
        soma = soma + valor
    else:
        soma = soma - valor

print("Total:", soma)