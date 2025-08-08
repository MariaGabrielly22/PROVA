numero_secreto = 22
palpite = int(input("Tente adivinhar o número secreto: "))

while palpite != numero_secreto:
    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    palpite = int(input("Tente adivinhar o número secreto: "))

print("Parabéns, você acertou!")
