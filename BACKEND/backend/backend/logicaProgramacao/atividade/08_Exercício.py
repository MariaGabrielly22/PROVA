numeros = [7, 3, 18, 22, 9, 1]

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("O maior número é:", maior)