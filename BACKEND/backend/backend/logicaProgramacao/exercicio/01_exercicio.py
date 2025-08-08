nome = input("Nome do usuário: ")
saldo = 0

print(f"Bem-vindo, {nome}")

opcao = ""
while opcao != "4":
    print("\n1. Depositar")
    print("2. Sacar")
    print("3. Ver Saldo")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1 a 4): ")
    
    match opcao:
        case "1":
            valor = int(input("Valor para depositar: "))
            if valor > 0:
                saldo += valor
                print("Depósito feito")
            else:
                print("Valor inválido")
                
        case "2":
            valor = int(input("Valor para sacar: "))
            if valor > 0:
                if valor <= saldo:
                    saldo -= valor
                    print("Saque feito")
                else:
                    print("Saldo insuficiente")
            else:
                print("Valor inválido")
                
        case "3":
            print(f"Saldo atual: R$ {saldo}")
            
        case "4":
            print(f"{nome}, tchau tchau beijinhos do Luan Santana")
            break
            
        case _:
            print("Opção inválida")