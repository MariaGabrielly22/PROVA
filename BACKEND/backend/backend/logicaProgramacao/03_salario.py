nome = input("Digite seu nome: ")
print("Olá,", nome)

salario = float(input("Digite o salário: "))

if salario == 5000:
    print("Classe Alta")

elif 3000 <=  salario  <= 4999:

    print("Classe Média")
elif salario < 300:

    print("Classe Baixa")
else:

    print("Valor inválido")