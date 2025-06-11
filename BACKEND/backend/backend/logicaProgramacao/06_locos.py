for i in range(11)
print("Contando", i)

numeros = [10, 15, 22, 33, 42, 55, 60, 73, 88, 91, 100]
pares = 0

for x in numeros:
    if( x % 2 == 0 ):
        pares+=1
        print("Quantidade de numeros pares:", pares)

soma = 0
Valor = 1

while Valor != 0:
    Valor = int(input("Digite um valor:"))
    soma+=valor

    print("Valor total da soma: ", soma)

    
senha = ""
while senha != "Splendore":
    senha = input("Digite a senha: ")
    if senha != "Splendore":
        print("Senha incorreta.")
print("Senha correta.")